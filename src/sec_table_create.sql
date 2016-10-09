CREATE TABLE sec_links 
(
     id serial,
     company_name varchar(200),
     form_type varchar(20),
     cik varchar(20) PRIMARY KEY,
     date date,
     link varchar(200),
     download_status bool
      );    