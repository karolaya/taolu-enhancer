//------------------------------------------------------------------------------
// Proyecto Final PDI 
// Autores: 
// Karolay Ardila
// Julián Sibaja
// Andrés Simancas
//------------------------------------------------------------------------------

#include "stdafx.h"
#include <strsafe.h>
#include "SkeletonBasics.h"
#include "resource.h"
#include <string>
#include <iostream>

using namespace std;

static const float g_JointThickness = 3.0f;
static const float g_TrackedBoneThickness = 6.0f;
static const float g_InferredBoneThickness = 1.0f;

int Connect2Kinect::Initialize()
{
	INuiSensor * pNuiSensor;
	
	// Look for kinect
	int iSensorCount = 0;
	HRESULT hr = NuiGetSensorCount(&iSensorCount);
	if (FAILED(hr)) {
		return 1;
	}
	return 1;
	/*
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
	}*/

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
	string Saludo("Successful, we have data");
	cout << Saludo;
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