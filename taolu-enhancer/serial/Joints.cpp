//------------------------------------------------------------------------------
// Proyecto Final PDI 
// Autores: 
// Karolay Ardila Salazar
// Julián Sibaja García
// Andrés Simancas Mateus
//------------------------------------------------------------------------------

#include "stdafx.h"
#include <strsafe.h>
#include "Joints.h"
#include "resource.h"
#include <stdint.h>
#include <string>
#include <sstream>
#include <iostream>

#define width 640
#define height 480

#define STANDBY_CODE 0
#define JOINTS_CODE 1
#define RGB_CODE 2
#define MAX_THREADS 2

HANDLE rgbStream;
const unsigned int N = height*width * 3 * 2;
BYTE dataRGB [width*height*4];
char p_data[width*height*4];

using namespace std;

static const float g_JointThickness = 3.0f;
static const float g_TrackedBoneThickness = 6.0f;
static const float g_InferredBoneThickness = 1.0f;
int index_joint[20] = {
	NUI_SKELETON_POSITION_HIP_CENTER,
	NUI_SKELETON_POSITION_SPINE,
	NUI_SKELETON_POSITION_SHOULDER_CENTER,
	NUI_SKELETON_POSITION_HEAD,
	NUI_SKELETON_POSITION_SHOULDER_LEFT,
	NUI_SKELETON_POSITION_ELBOW_LEFT,
	NUI_SKELETON_POSITION_WRIST_LEFT,
	NUI_SKELETON_POSITION_HAND_LEFT,
	NUI_SKELETON_POSITION_SHOULDER_RIGHT,
	NUI_SKELETON_POSITION_ELBOW_RIGHT,
	NUI_SKELETON_POSITION_WRIST_RIGHT,
	NUI_SKELETON_POSITION_HAND_RIGHT,
	NUI_SKELETON_POSITION_HIP_LEFT,
	NUI_SKELETON_POSITION_KNEE_LEFT,
	NUI_SKELETON_POSITION_ANKLE_LEFT,
	NUI_SKELETON_POSITION_FOOT_LEFT,
	NUI_SKELETON_POSITION_HIP_RIGHT,
	NUI_SKELETON_POSITION_KNEE_RIGHT,
	NUI_SKELETON_POSITION_ANKLE_RIGHT,
	NUI_SKELETON_POSITION_FOOT_RIGHT
};
float x;
float y;
float z;
string datos = "";
int py_message = STANDBY_CODE;
int counter = 0;

typedef struct IOPacket {
	int py_input;
} packet, *Packet;

int Connect2Kinect::Initialize()
{
	INuiSensor * pNuiSensor;
	
	// Look for kinect
	int iSensorCount = 0;
	HRESULT hr = NuiGetSensorCount(&iSensorCount);
	if (FAILED(hr)) {
		return 1;
	}
	
	// Iterate over the kinects found
	for(int i = 0; i < iSensorCount; ++i) {
		// Create the sensor to check the status, if we can not, move onto the next
		hr = NuiCreateSensorByIndex(i, &pNuiSensor);
		if (FAILED(hr)) {
			continue;
		}

		// Check status, if connected, we can initialize it.
		hr = pNuiSensor->NuiStatus();
		if (S_OK == hr)
		{
			m_pNuiSensor = pNuiSensor;
			break;
		}

		// If this line is reached the sensor was not ok, so release it
		pNuiSensor->Release();
	}

	if (NULL != m_pNuiSensor) {
		// Initialize the Kinect and use it for skeleton and RGB image
		hr = m_pNuiSensor->NuiInitialize(NUI_INITIALIZE_FLAG_USES_SKELETON | NUI_INITIALIZE_FLAG_USES_COLOR);
		if (SUCCEEDED(hr)) {
			// Create an event that will be called each time there is data available
			m_hNextSkeletonEvent = CreateEventW(NULL, TRUE, FALSE, NULL);

			// Open a skeleton stream to receive skeleton data
			hr = m_pNuiSensor->NuiSkeletonTrackingEnable(m_hNextSkeletonEvent, 0);
			m_pNuiSensor->NuiImageStreamOpen(
				NUI_IMAGE_TYPE_COLOR,            // Depth camera or rgb camera?
				NUI_IMAGE_RESOLUTION_640x480,    // Image resolution
				0,      // Image stream flags, e.g. near mode
				2,      // Number of frames to buffer
				NULL,   // Event handle
				&rgbStream);
		}
	}

	if (NULL == m_pNuiSensor || FAILED(hr)) {
		return 2;
	}

	return 0;
};

void Connect2Kinect::Update(int data_type)
{
	if (NULL == m_pNuiSensor)
	{
		return;
	}

	// Access to ProcessData method
	if (WAIT_OBJECT_0 == WaitForSingleObject(m_hNextSkeletonEvent, 0))
	{
		if (data_type == JOINTS_CODE) {
			ProcessData();
		}
		else{
			getDataRGB(p_data);
				char dummy[3 * width * height];

				// Pointer to the first element of array
				char * ini_ptr = &dummy[0];

				// Expand array
				int j;
				//for (int i = 0; i < height; ++i) {
					j = 0;
					for (int k = 0; k < 4 * width * height; k = k + 4) {
						// r,g,b,a,r,g,b,a,...
						dummy[j] = p_data[k];
						dummy[j + 1] = p_data[k + 1];
						dummy[j + 2] = p_data[k + 2];
						j = j + 3;
					}
					fwrite(ini_ptr, sizeof(char), 3 * width * height, stdout);
					fflush(stdout);
					cout << endl;
				//}
			// [¡] Send to python here [!]
		}
	}
}

void Connect2Kinect::ProcessData(void) 
{
	// Create the frame
	NUI_SKELETON_FRAME skeletonFrame = { 0 };
	HRESULT hr = m_pNuiSensor->NuiSkeletonGetNextFrame(0, &skeletonFrame);
	if (FAILED(hr)) {
		return;
	}

	// Smooth the obtained skeleton data
	m_pNuiSensor->NuiTransformSmooth(&skeletonFrame, NULL);	

	getData(&skeletonFrame);

	//string Saludo("Successful, we have data\n");
	//cout << Saludo;
}

void Connect2Kinect::getData(NUI_SKELETON_FRAME* sframe)
{
	int drop_frame;
	for (int i = 0; i < NUI_SKELETON_COUNT; ++i) {
		const NUI_SKELETON_DATA &skeleton = sframe->SkeletonData[i];

		// Extract skeleton joints
		drop_frame = 0;
		for (int k = 0; k < 20; ++k) {
			x = skeleton.SkeletonPositions[index_joint[k]].x;
			y = skeleton.SkeletonPositions[index_joint[k]].y;
			z = skeleton.SkeletonPositions[index_joint[k]].z;

			if (x != 0 && y != 0 && z != 0) {
				ostringstream oss;
				oss << x << "," << y << "," << z << ";";
				datos = oss.str() + datos;
			}
			else {
				drop_frame = 1;
				break;
			}
		}
		//printf(datos);
		if (drop_frame == 0 && !datos.empty()) {
			cout << datos << "\n";
		}
		datos = "";
	}
}

int Connect2Kinect::getDataRGB(char *pdata){
	NUI_IMAGE_FRAME imageFrame;
	NUI_LOCKED_RECT LockedRect; // Pointer to the data
	if (m_pNuiSensor->NuiImageStreamGetNextFrame(rgbStream, 0, &imageFrame) < 0) return 1;
	INuiFrameTexture* texture = imageFrame.pFrameTexture;
	texture->LockRect(0, &LockedRect, NULL, 0);
	// Check if if not empty, if its not the save data into "data"
	if (LockedRect.Pitch != 0)
	{
		 BYTE* curr = (BYTE*)LockedRect.pBits;
		BYTE* dataEnd = curr + (width*height) * 4;

		for (int i = 0; i < width*height*4; ++i) {
			if (((int)*curr) > 216 && ((int)*curr) < 222) {
				pdata[i] = '0' + 255;
			}
			else {
				pdata[i] = '0' + (((int)*curr));
			}
			++curr;
		}
	}
	texture->UnlockRect(0);
	m_pNuiSensor->NuiImageStreamReleaseFrame(rgbStream, &imageFrame);
	return 0;
}


DWORD WINAPI readPythonInput(LPVOID lpParam) {
	while (1) {
		if (!feof(stdin)) {
			cin >> py_message;
		}
	}
	
	return 0;
}

void createReadingThread() {
	Packet p_data;
	DWORD thread_id;
	HANDLE h_thread;
	
	p_data = (Packet) HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, sizeof(Packet));

	if (p_data == NULL) {
			ExitProcess(2);
	}

	p_data->py_input = STANDBY_CODE;
	h_thread = CreateThread(NULL, 0, readPythonInput, p_data, 0, &thread_id);

	if (h_thread == NULL) {
		ExitProcess(3);
	}
}


int main() {
	Connect2Kinect cc;
	int ini = cc.Initialize();

	if (ini == 1) {
		string Fail1("No se ha encontrado kinect");
		cout << Fail1;
	}
	else if (ini == 2) {
		string Fail("No se encuentra disponible Kinect");
		cout << Fail;
	}
	else if (ini == 0) {
		string Saludo("Conexion exitosa\n");
		cout << Saludo;

		createReadingThread();

		while (1) {
			if (py_message == STANDBY_CODE) {
				// :v pos no hago nada
			}
			else if (py_message == JOINTS_CODE) {
				cc.Update(JOINTS_CODE);
			}
			else if (py_message == RGB_CODE) {
				cc.Update(RGB_CODE);
			}
		}
	}

	return 0;
}