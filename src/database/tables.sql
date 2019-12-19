--
-- Database creation Script
-- Energyblast project
-- DS4A Colombia  Team 23
-- 

--
-- month_demand table 
--

drop table month_demand;

create table month_demand(
	fecha date primary key,
	demanda float ,
	generacion float);

--
-- month_inflow table 
--
drop table month_inflow;

create table month_inflow(
	 region varchar(100), rio varchar(100),fecha date,aportes float)
	;
alter table month_inflow add primary key (fecha, region, rio);

--
-- month_offer table 
--

drop table month_offer;

create table month_offer(
agente varchar(4),
tipo varchar(20),
recurso varchar(100),
fecha date,
oferta float);

alter table month_offer add primary key (fecha, agente,tipo, recurso);

--
-- month_precipitation table 
--

drop table month_precipitation;

create table month_precipitation(
fecha date,region varchar(100),recurso varchar(100),embalse varchar(100),precipitacion float);

alter table month_precipitation add primary key (fecha, region, recurso, embalse);

--
-- month_spill table 
--	

drop table month_spill;

create table month_spill(
	region varchar(100),embalse varchar(100),fecha date,vertimiento float);
	
alter table month_spill add primary key (fecha, region, embalse);

--
-- month_price table 
--	

drop table month_price;
	
create table month_price(
	fecha date primary key, precio float,open float,close float,high float,low float);

--
-- month_storage table 
--	

drop table month_storage;

create table month_storage(
	a integer, fecha date, region varchar(100),embalse varchar(100),vol_util float);
	
alter table month_storage add primary key (region, fecha, embalse);

--
-- month_noaa table 
--	

drop table month_noaa;

create table month_noaa
(fecha date primary key,censo float,nao float,nina1 float,nina3 float,nina34 float,nina4 float,pna float,qbo float,soi float,solar float,tna float,tsa float,whwp float,wp float);

--
-- month_offer table 
--	

create table recurso_region(
recurso varchar(100) primary key, region varchar(100));

--
-- stantdarize column to upper values
--
-- update recurso_region set region = upper(region)


-- update month_offer o set region = (select region from recurso_region where recurso = o.recurso);



