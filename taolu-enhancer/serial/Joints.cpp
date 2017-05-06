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

#include <string>
#include <sstream>
#include <iostream>

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
		// Initialize the Kinect and use it for skeleton
		hr = m_pNuiSensor->NuiInitialize(NUI_INITIALIZE_FLAG_USES_SKELETON);
		if (SUCCEEDED(hr)) {
			// Create an event that will be called each time there is data available
			m_hNextSkeletonEvent = CreateEventW(NULL, TRUE, FALSE, NULL);

			// Open a skeleton stream to receive skeleton data
			hr = m_pNuiSensor->NuiSkeletonTrackingEnable(m_hNextSkeletonEvent, 0);
		}
	}

	if (NULL == m_pNuiSensor || FAILED(hr)) {
		return 2;
	}

	return 0;
};

void Connect2Kinect::Update(void)
{
	if (NULL == m_pNuiSensor)
	{
		return;
	}

	// Access to ProcessData method
	if (WAIT_OBJECT_0 == WaitForSingleObject(m_hNextSkeletonEvent, 0))
	{
		ProcessData();
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

	string Saludo("Successful, we have data\n");
	//cout << Saludo;
}

void Connect2Kinect::getData(NUI_SKELETON_FRAME* sframe)
{
	for (int i = 0; i < NUI_SKELETON_COUNT; ++i) {
		const NUI_SKELETON_DATA &skeleton = sframe->SkeletonData[i];

		// Extract skeleton joints
		for (int k = 0; k < 20; ++k) {
			x = skeleton.SkeletonPositions[index_joint[k]].x;
			y = skeleton.SkeletonPositions[index_joint[k]].y;
			z = skeleton.SkeletonPositions[index_joint[k]].z;

			if (x != 0 && y != 0 && z != 0) {
				ostringstream oss;
				oss << x << "," << y << "," << z << ";";
				datos = oss.str() + datos;
			}
		}
		//printf(datos);
		if (!datos.empty()) {
			cout << datos << "\n";
		}
		datos = "";
	}
}

int main() {
	Connect2Kinect cc;
	int ini = cc.Initialize();

	if (ini == 1) {
		string Fail1("No kinect found");
		cout << Fail1;
	}
	else if (ini == 2) {
		string Fail("No ready Kinect found!");
		cout << Fail;
	}
	else if (ini == 0) {
		while (1) {
			cc.Update();
		}
	}
	while (1);
	return 0;
}