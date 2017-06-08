#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import ctre #This is for the CANTalons

class Robot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #self.talon_FL = ctre.CANTalon(1) #These are what should be used -- CANTalons
        #self.talon_ML = ctre.CANTalon(2)
        #self.talon_RL = ctre.CANTalon(3)
        #self.talon_FR = ctre.CANTalon(4)
        #self.talon_MR = ctre.CANTalon(5)
        #self.talon_RR = ctre.CANTalon(6)
        self.talon_FL = wpilib.Talon(1) #These are what works with the simulation -- Talons
        self.talon_ML = wpilib.Talon(2)
        self.talon_RL = wpilib.Talon(3)
        self.talon_FR = wpilib.Talon(4)
        self.talon_MR = wpilib.Talon(5)
        self.talon_RR = wpilib.Talon(6)
        self.drive_train = wpilib.RobotDrive(self.talon_FL, self.talon_RL,
                                             self.talon_FR, self.talon_RR)

        #The wpilib.RobotDrive() method only takes in two or four motors
        #My solution is putting the other two in follower mode
        #I believe this will work because in the documentation, all of the
        #Different functions that actually move the robot, ArcadeDrive, TankDrive,
        #and just normal drive all use setLeftRightMotorOutputs to actually set
        #The talons. For the four motors used in the constructor above, it just
        #Sets those normally with that method. For the other two, the set method
        #Can be used manually with the port of the talon to follow

        self.talon_ML.setControlMode(CANTalon.ControlMode.Follower)
        self.talon_RL.setControlMode(CANTalon.ControlMode.Follower)

        self.driver = wpilib.Joystick(0) #Driver is port 0
        self.gunner = wpilib.Joystick(1) #Gunner is port 1, currently not used

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.drive_train.arcadeDrive(-1.0, 0.0)
            self.auto_loop_counter += 1
            self.talon_ML.set(1) #follows self.talon_FL
            self.talon_MR.set(4) #follows self.talon_FR
        else:
            self.drive_train.arcadeDrive(0.0, 0.0)
            self.talon_ML.set(1) #follows self.talon_FL
            self.talon_MR.set(4) #follows self.talon_FR

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass
        #self.robot_drive.arcadeDrive(self.stick)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(Robot, physics_enabled=True)
