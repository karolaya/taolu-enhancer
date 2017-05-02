/*
	This algorithm creates a pose-book for the training set. It assumes a finite number of pages: 100.
	Each pose is identified by 13 features, and will be repeated 10.
*/

#include <stdio.h>
#include "lib/descriptor.h"

float* Pose::getPoseAngles()
{
	return angles;
}

void Pose::setPoseAngles(float ang[ANGLE_COUNT])
{
	angles = ang;
}

float* Pose::getPoseJoints()
{
	return joints;
}

void Pose::setPoseJoints(float jnt[JOINT_COUNT])
{
	joints = jnt;
}

float Pose::getEuclideanMean()
{
	return 4.32F;
}

int main()
{
	float a[ANGLE_COUNT];
	float j[JOINT_COUNT];
	float l = 0;

	for(int i = 0; i < ANGLE_COUNT; ++i) {
		a[i] = i*2;
	}

	for(int i = 0; i < JOINT_COUNT; ++i) {
		j[i] = i+1;
	}

	Pose pose;
	pose.setPoseAngles(a);
	pose.setPoseJoints(j);
	l = pose.getEuclideanMean();

	printf("%f\n", l);

	float* k;
	k = pose.getPoseAngles();
	for(int i = 0; i < ANGLE_COUNT; ++i) {
		printf("%f ", k[i]);
	}
	printf("\n");

	return 0;
}
