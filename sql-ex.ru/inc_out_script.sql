create database inc_out
go
use inc_out
GO
PRINT N'Recreating the objects for the database'
--Drop all FKs in the database
declare @table_name sysname, @constraint_name sysname
declare i cursor static for 
select c.table_name, a.constraint_name
from INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS a join INFORMATION_SCHEMA.KEY_COLUMN_USAGE b
on a.unique_constraint_name=b.constraint_name join INFORMATION_SCHEMA.KEY_COLUMN_USAGE c
on a.constraint_name=c.constraint_name
WHERE upper(c.table_name) in (upper('Income'),upper('Outcome'),upper('Income_o'),upper('Outcome_o'))
open i
fetch next from i into @table_name,@constraint_name
while @@fetch_status=0
begin
	exec('ALTER TABLE '+@table_name+' DROP CONSTRAINT '+@constraint_name)
	fetch next from i into @table_name,@constraint_name
end
close i
deallocate i
GO
--Drop all tables
declare @object_name sysname, @sql varchar(8000)
declare i cursor static for 
SELECT table_name from INFORMATION_SCHEMA.TABLES
where upper(table_name) in (upper('Income'),upper('Outcome'),upper('Income_o'),upper('Outcome_o'))

open i
fetch next from i into @object_name
while @@fetch_status=0
begin
	set @sql='DROP TABLE [dbo].['+@object_name+']'
	exec(@sql)
	fetch next from i into @object_name
end
close i
deallocate i
GO

CREATE TABLE [dbo].[Income] (
	[code] [int] NOT NULL ,
	[point] [tinyint] NOT NULL ,
	[date] [datetime] NOT NULL ,
	[inc] [smallmoney] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Outcome] (
	[code] [int] NOT NULL ,
	[point] [tinyint] NOT NULL ,
	[date] [datetime] NOT NULL ,
	[out] [smallmoney] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Income_o] (
	[point] [tinyint] NOT NULL ,
	[date] [datetime] NOT NULL ,
	[inc] [smallmoney] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Outcome_o] (
	[point] [tinyint] NOT NULL ,
	[date] [datetime] NOT NULL ,
	[out] [smallmoney] NOT NULL 
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Income] WITH NOCHECK ADD 
	CONSTRAINT [PK_Income] PRIMARY KEY  NONCLUSTERED 
	(
		[code]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[Outcome] WITH NOCHECK ADD 
	CONSTRAINT [PK_Outcome] PRIMARY KEY  NONCLUSTERED 
	(
		[code]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[Income_o] WITH NOCHECK ADD 
	CONSTRAINT [PK_Income_o] PRIMARY KEY  NONCLUSTERED 
	(
		[point],
		[date]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[Outcome_o] WITH NOCHECK ADD 
	CONSTRAINT [PK_Outcome_o] PRIMARY KEY  NONCLUSTERED 
	(
		[point],
		[date]
	)  ON [PRIMARY] 
GO
                                                                                                                                                                                                                                                                 
----Income------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
insert into Income values(1,1,'20010322 00:00:00.000',15000.00)
insert into Income values(2,1,'20010323 00:00:00.000',15000.00)
insert into Income values(3,1,'20010324 00:00:00.000',3600.00)
insert into Income values(4,2,'20010322 00:00:00.000',10000.00)
insert into Income values(5,2,'20010324 00:00:00.000',1500.00)
insert into Income values(6,1,'20010413 00:00:00.000',5000.00)
insert into Income values(7,1,'20010511 00:00:00.000',4500.00)
insert into Income values(8,1,'20010322 00:00:00.000',15000.00)
insert into Income values(9,2,'20010324 00:00:00.000',1500.00)
insert into Income values(10,1,'20010413 00:00:00.000',5000.00)
insert into Income values(11,1,'20010324 00:00:00.000',3400.00)
insert into Income values(12,3,'20010913 00:00:00.000',1350.00)
insert into Income values(13,3,'20010913 00:00:00.000',1750.00)

GO

                                                                                                                                                                                                                                                                 
----Outcome---------------------------------------------------------- 
insert into Outcome values(1,1,'20010314 00:00:00.000',15348.00)
insert into Outcome values(2,1,'20010324 00:00:00.000',3663.00)
insert into Outcome values(3,1,'20010326 00:00:00.000',1221.00)
insert into Outcome values(4,1,'20010328 00:00:00.000',2075.00)
insert into Outcome values(5,1,'20010329 00:00:00.000',2004.00)
insert into Outcome values(6,1,'20010411 00:00:00.000',3195.04)
insert into Outcome values(7,1,'20010413 00:00:00.000',4490.00)
insert into Outcome values(8,1,'20010427 00:00:00.000',3110.00)
insert into Outcome values(9,1,'20010511 00:00:00.000',2530.00)
insert into Outcome values(10,2,'20010322 00:00:00.000',1440.00)
insert into Outcome values(11,2,'20010329 00:00:00.000',7848.00)
insert into Outcome values(12,2,'20010402 00:00:00.000',2040.00)
insert into Outcome values(13,1,'20010324 00:00:00.000',3500.00)
insert into Outcome values(14,2,'20010322 00:00:00.000',1440.00)
insert into Outcome values(15,1,'20010329 00:00:00.000',2006.00)
insert into Outcome values(16,3,'20010913 00:00:00.000',1200.00)
insert into Outcome values(17,3,'20010913 00:00:00.000',1500.00)
insert into Outcome values(18,3,'20010914 00:00:00.000',1150.00)

GO

                                                                                                                                                                                                                                                                 
----Income_o----------------------------------------------------------
insert into Income_o values(1,'20010322 00:00:00.000',15000.00)
insert into Income_o values(1,'20010323 00:00:00.000',15000.00)
insert into Income_o values(1,'20010324 00:00:00.000',3400.00)
insert into Income_o values(1,'20010413 00:00:00.000',5000.00)
insert into Income_o values(1,'20010511 00:00:00.000',4500.00)
insert into Income_o values(2,'20010322 00:00:00.000',10000.00)
insert into Income_o values(2,'20010324 00:00:00.000',1500.00)
insert into Income_o values(3,'20010913 00:00:00.000',11500.00)
insert into Income_o values(3,'20011002 00:00:00.000',18000.00)

GO

                                                                                                                                                                                                                                                                 
----Outcome_o----------------------------------------------------------
insert into Outcome_o values(1,'20010314 00:00:00.000',15348.00)
insert into Outcome_o values(1,'20010324 00:00:00.000',3663.00)
insert into Outcome_o values(1,'20010326 00:00:00.000',1221.00)
insert into Outcome_o values(1,'20010328 00:00:00.000',2075.00)
insert into Outcome_o values(1,'20010329 00:00:00.000',2004.00)
insert into Outcome_o values(1,'20010411 00:00:00.000',3195.04)
insert into Outcome_o values(1,'20010413 00:00:00.000',4490.00)
insert into Outcome_o values(1,'20010427 00:00:00.000',3110.00)
insert into Outcome_o values(1,'20010511 00:00:00.000',2530.00)
insert into Outcome_o values(2,'20010322 00:00:00.000',1440.00)
insert into Outcome_o values(2,'20010329 00:00:00.000',7848.00)
insert into Outcome_o values(2,'20010402 00:00:00.000',2040.00)
insert into Outcome_o values(3,'20010913 00:00:00.000',1500.00)
insert into Outcome_o values(3,'20010914 00:00:00.000',2300.00)
insert into Outcome_o values(3,'20020916 00:00:00.000',2150.00)

GO

