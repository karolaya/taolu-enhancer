#define ANGLE_COUNT 13
#define JOINT_COUNT 20
#define ANGLE_NECK_TORSO 1
#define ANGLE_SHOULDER_ARM_R 2
#define ANGLE_SHOULDER_ARM_L 3
#define ANGLE_ARM_ARM_R 4
#define ANGLE_ARM_ARM_L 5
#define ANGLE_HIP_LEG_R 6
#define ANGLE_HIP_LEG_L 7
#define ANGLE_LEG_LEG_R 8
#define ANGLE_LEG_LEG_L 9
#define ANGLE_ARM_HIPLINE_R 10
#define ANGLE_ARM_HIPLINE_L 11
#define ANGLE_THIGH_HIPLINE_R 12
#define ANGLE_THIGH_HIPLINE_L 13

/*
	Pose class defines a normalized way to represent a pose.
	It has the angle array, the joint's position array, a method to calculate the
	euclidean mean of angles.
*/
class Pose
{
private:
	float *angles;
	float *joints;
public:
	Pose() {
		angles = new float[ANGLE_COUNT];
		joints = new float[JOINT_COUNT];
	}

	float* getPoseAngles();
	void setPoseAngles(float *ang);

	float* getPoseJoints();
	void setPoseJoints(float *joint);

	float getEuclideanMean();

/*~Pose() {
	delete angles;
	delete joints;
}*/
};