create database futurense;
use futurense;


create table Student(
S_id int Primary key,
S_name varchar(30) not null,
Degree varchar(30) not null,
Batch int not null,
Ongoingsem int not null,
Rollno varchar(30) not null unique,
Section varchar(30) not null,
Phone1 varchar(30) unique not null,
Email varchar(50) unique not null ,
Address varchar(30) not null);




create table Login(
L_id int primary key,
S_id int,
foreign key(S_id) references Student(S_id),
Password varchar(30) not null);




create table Teachers(
T_id int primary key,
T_name varchar(30) not null);



CREATE TABLE Grades (
    G_id INT PRIMARY KEY,
    S_id INT,
    C_id INT,
    Grade CHAR(2) NOT NULL,
    FOREIGN KEY (S_id) REFERENCES Student(S_id),
    FOREIGN KEY (C_id) REFERENCES Courses(C_id)
);



create table Courses(
C_id int primary key,
C_name varchar(50) not null unique,
T_id int,
foreign key(T_id) references Teachers(T_id));

alter table Courses
add column image_path varchar(50);

create table Enrollement(
E_id int primary key,
C_id int,
S_id int,
foreign key(S_id) references Student(S_id),
foreign key(C_id) references Courses(C_id));


create table LearningSpace(
Ls_id int primary key,
Title varchar(30) not null,
C_id int,
foreign key(C_id) references Courses(C_id),
Filedata varchar(50) not null);


create table Message(
M_id int primary key,
S_id int,
foreign key(S_id) references Student(S_id),
T_id int,
foreign key(T_id) references Teachers(T_id),
Msg TEXT NOT NULL);


create table Assignment(
A_id int primary key,
A_name varchar(30) not null,
C_id int,
foreign key(C_id) references Courses(C_id),
Filedata varchar(30) NOT NULL);



INSERT INTO Student (S_id, S_name, Degree, Batch, Ongoingsem, Rollno, Section, Phone1, Email, Address) VALUES
(991, 'Gurkirat Singh', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE57', 'K23FE', '9888296690', 'Gurkirat0001@gmail.com', ' Amritsar'),
(992, 'Harsha', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE29', 'K23FE', '9592342001', 'Reddy4545@gmail.com', 'Ludhiana'),
(993, 'Madhav', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE07', 'K23FE', '6284844542', 'madhav0001@gmail.com', 'Jalandhar'),
(994, 'Prathamesh', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE52', 'K23FE', '7814317944', 'prathamesh6767@gmail.com', 'Amritsar'),
(995, 'Adwaid', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE32', 'K23FE', '9478592165', 'Adwaid995@gmail.com', 'Patiala');

INSERT INTO Student VALUES (996, 'Arpita', 'Btech(Cse) AI and DE', 2023, 3, 'RK23FE45', 'K23FE', '9478545152', 'Arpita345@gmail.com', 'Sonipath');



INSERT INTO Login (L_id, S_id, Password) VALUES
(12315135, 991, 'abcde'),
(12315136, 992, 'abcdf'),
(12315137, 993, 'abcdg'),
(12315138, 994, 'abcdh'),
(12315139, 995, 'abcdi');

INSERT INTO Student VALUES (12315140,996,'abcdt');




INSERT INTO Teachers (T_id, T_name) VALUES
(111, 'Ziyaad Sir'),
(112, 'Neelam mam'),
(113, 'Simran mam');



INSERT INTO Courses (C_id, C_name, T_id) VALUES
(771, 'DSA', 111),
(772, 'Data communication', 113),
(773, 'Mathematics', 112),
(774, 'DBMS', 111);

update Courses
set image_path = "images/c2.jpeg"
where C_id = 774;

update Courses
set image_path = "images/c1.jpeg"
where C_id = 773;

update Courses
set image_path = "images/c3.jpeg"
where C_id = 771;

update Courses
set image_path = "images/c4.jpeg"
where C_id = 772;

INSERT INTO Enrollement (E_id, S_id, C_id) VALUES
(1001, 991, 771),
(1002, 992, 771),
(1003, 993, 771),
(1004, 994, 771),
(1005, 995, 771),
(1006, 991, 772),
(1007, 992, 772),
(1008, 993, 772),
(1009, 994, 772),
(1010, 995, 772),
(1011, 991, 773),
(1012, 992, 773),
(1013, 993, 773),
(1014, 994, 773),
(1015, 995, 773),
(1016, 991, 774),
(1017, 992, 774),
(1018, 993, 774),
(1019, 994, 774),
(1020, 995, 774);



INSERT INTO Grades (G_id, S_id, C_id, Grade) VALUES
(1, 991, 771, 'A'),
(2, 991, 772, 'B+'),
(3, 991, 773, 'A+'),
(4, 992, 772, 'B'),
(5, 992, 773, 'A'),
(6, 992, 774, 'B+'),
(7, 993, 771, 'B+'),
(8, 993, 774, 'A'),
(9, 994, 771, 'A'),
(10, 994, 773, 'B+'),
(11, 995, 774, 'A'),
(12, 996, 771, 'A'),
(13, 996, 772, 'B+'),
(14, 996, 774, 'A');

delete from Enrollement
where E_id = 1002;

delete from Enrollement
where E_id = 1006;

delete from Enrollement
where E_id = 1013;

delete from Enrollement
where E_id = 1019;



INSERT INTO Enrollement (E_id, S_id, C_id) VALUES
(1002, 996,771),
(1006,996,772),
(1013,996,774);





INSERT INTO LearningSpace (Ls_id, Title, C_id, Filedata) VALUES
(331, 'Unit-1', 772, 'D:/pdf/1.pdf'), 
(332, 'Unit-2', 772, 'D:/pdf/2.pdf'), 
(333, 'unit-3', 771, 'D:/pdf/3.pdf'), 
(334, 'Viva Description', 771, 'D:/pdf/4.pdf'), 
(335, 'project guide', 771, 'D:/pdf/5.pdf'), 
(336, 'Unit-5', 774, 'D:/pdf/6.pdf'), 
(337, 'unit-2', 773, 'D:/pdf/7.pdf');


INSERT INTO Message (M_id, S_id, T_id, Msg)
VALUES
	(554, 992, 112, 'Welcome to Futurense'),
    (555, 992, 111, 'hhhhhcsdn mi jndsnck n ononnds n'),
    (556, 994, 112, 'kkshnlml cklmojm lkos'),
    (557, 994, 111, 'njkscsbkBKn m m kjnkjc b j kj s'),
    (558, 993, 113, 'kljlnlk;ncm jninbid'),
    (559, 993, 111, 'njcknnn kmkmkok noikndl');

INSERT INTO Message (M_id, S_id, T_id, Msg)
VALUES
	(552, 991, 112, 'Welcome to Futurense'),
    (553, 991, 111, 'You semster will start from 30th july!!!');


INSERT INTO Assignment (A_id, A_name, C_id, Filedata)
VALUES
    (221, 'DSA-1', 771,'D:/pdf/1.pdf' ),
    (222, 'Maths-1', 773,"D:/pdf/2.pdf" ),
    (223, 'Dsa-2', 771, "D:/pdf/3.pdf"),
    (224, 'Dsa-3', 771, "D:/pdf/4.pdf"),
    (225, 'DBMS', 774, "D:/pdf/5.pdf");


