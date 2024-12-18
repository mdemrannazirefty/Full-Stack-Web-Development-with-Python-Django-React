CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorName VARCHAR(100) NOT NULL,
    DoctorSpecialization VARCHAR(255) NOT NULL,
    DoctorPhone VARCHAR(11) NOT NULL
);
INSERT INTO Doctors (DoctorName, DoctorSpecialization, DoctorPhone) VALUES
    ('Efty', 'Cardiologist', '01675889465'),
    ('Emran', 'Pediatrician', '01786991542'),
    ('Mohammad', 'Orthopedic Surgeon', '01945778426'),
    ('Rafi', 'Dermatologist', '01889475260'),
    ('Nazir', 'Neurologist', '01678542685');


CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    PatienName VARCHAR(100) NOT NULL,
    PatienAge INT NOT NULL,
    PatienGender CHAR(1) NOT NULL,
    PatienPhone VARCHAR(11) NOT NULL
);
INSERT INTO Patients (PatienName, PatienAge, PatienGender, PatienPhone) VALUES
    ('Safa', 25, 'F', '01678554963'),
    ('Malwk', 40, 'M', '01758423658'),
    ('Roton', 60, 'M', '01784884257'),
    ('Sadia', 35, 'F', '01975362485'),
    ('Ishraq', 50, 'M', '01348526792');


CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);
INSERT INTO Departments (DepartmentName, Location) VALUES
    ('Cardiology', 'Building A, Room-101'),
    ('Pediatrics', 'Building A, Room-102'),
    ('Orthopedics', 'Building A, Room-103'),
    ('Dermatology', 'Building A, Room-104'),
    ('Neurology', 'Building A, Room-105');


CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorID INT,
    PatientID INT,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO Appointments (DoctorID, PatientID, Date, Time, Status) VALUES
    (1, 521, '2024-12-19', '10:00:00', 'Booked'), 
    (2, 522, '2024-12-20', '11:30:00', 'Booked'), 
    (3, 523, '2024-12-19', '14:00:00', 'Booked'), 
    (4, 524, '2024-12-21', '09:00:00', 'Booked'), 
    (5, 525, '2024-12-22', '15:30:00', 'Booked'); 


CREATE TABLE Doctor_Departments (
    DoctorID INT,
    DepartmentID INT,
    PRIMARY KEY (DoctorID, DepartmentID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO Doctor_Departments (DoctorID, DepartmentID) VALUES
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 4), 
    (5, 5); 