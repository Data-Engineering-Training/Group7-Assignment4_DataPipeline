CREATE TABLE "Account" (
  "Account_ID" int PRIMARY KEY,
  "Customer_ID" int,
  "Account_Type" varchar,
  "Balance" decimal,
  "Open_Date" timestamp,
  "Status" varchar
);

CREATE TABLE "Transaction" (
  "Transaction_ID" int PRIMARY KEY,
  "Account_ID" int,
  "Transaction_Type" varchar,
  "Amount" decimal,
  "Transaction_Date" timestamp,
  "Description" varchar
);

CREATE TABLE "Loan" (
  "Loan_ID" int PRIMARY KEY,
  "Customer_ID" int,
  "Loan_Type" varchar,
  "Amount" decimal,
  "Interest_Rate" decimal,
  "Term" int,
  "Start_Date" timestamp,
  "Status" varchar
);

CREATE TABLE "Payment" (
  "Payment_ID" int PRIMARY KEY,
  "Loan_ID" int,
  "Amount" decimal,
  "Payment_Date" timestamp
);

CREATE TABLE "Customer" (
  "Customer_ID" int PRIMARY KEY,
  "First_Name" varchar,
  "Last_Name" varchar,
  "Date_of_Birth" date,
  "Address" varchar,
  "Phone_Number" varchar,
  "Email" varchar,
  "KYC_Details" varchar
);

CREATE TABLE "Employee" (
  "Employee_ID" int PRIMARY KEY,
  "First_Name" varchar,
  "Last_Name" varchar,
  "Position" varchar,
  "Date_of_Hire" date,
  "Salary" decimal
);

CREATE TABLE "Branch" (
  "Branch_ID" int PRIMARY KEY,
  "Branch_Name" varchar,
  "Location" varchar,
  "Phone_Number" varchar,
  "Manager_ID" int
);

ALTER TABLE "accounts" ADD FOREIGN KEY ("Customer_ID") REFERENCES "customers" ("Customer_ID");

ALTER TABLE "transactions" ADD FOREIGN KEY ("Account_ID") REFERENCES "accounts" ("Account_ID");

ALTER TABLE "loans" ADD FOREIGN KEY ("Customer_ID") REFERENCES "customers" ("Customer_ID");

ALTER TABLE "payments" ADD FOREIGN KEY ("Loan_ID") REFERENCES "loans" ("Loan_ID");

ALTER TABLE "branches" ADD FOREIGN KEY ("Manager_ID") REFERENCES "employees" ("Employee_ID");
