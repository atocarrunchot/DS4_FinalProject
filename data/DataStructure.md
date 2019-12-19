# Data Structure

## Demanda

- Data 2018-2019 in folder (Same files)
- Data from 2000-2017 Inside folders

### Demanda/Demanda Comercial

* Demanda_Comercial_No_Regulada_Por_CIIU_2000*.xlsx : Contains the information of demand (KwH) by comercial activity (CIIU) - sub activity per day (Each file has Trimester data)

|Fecha|CIIU|Sub Actividad|Demanda Comercial kWh|Version|
|-----|----|-------------|---------------------|-------|

* Demanda_Comercial_Por_Comercializador_*.xlsx: Contains demand info (I assume KwH) by comercializador, Market and day (Each file has semester data)

|Fecha|Codigo Comercializador|Mercado|0-23|Version|
|-----|----------------------|-------|----|-------|

* Demanda_por_OR_*.xlsx: Contains demand info (I assume KwH) by distribuitor and day (Each file has 1 year data)

|Fecha|Código Distribuidor|0-23|Version|
|-----|-------------------|----|-------|

* Perdidas_De_Energia_Por_Comercializador_*.xlsx: Contains Energy loss info (I assume KwH) by comercializadorand day (Each file has 1 year data)

|Fecha|Código Comercializador|0-23|Version|
|-----|----------------------|----|-------|


**All files except CIIU have the same format (Some files have a version column)**

	- What does Version mean? TX3,TX4 etc.
___

### Demanda/Demanda Nacional

* Demanda_Energia_SIN_*.xlsx: Contains daily demand, generation, non-fullfiled demand, exports and imports of energy (Each file has 1 year data)

|Fecha|Demanda Energia SIN kWh|Generación kWh|Demanda No Atendida kWh|Exportaciones kWh|Importaciones kWh|
|-----|-----------------------|--------------|-----------------------|-----------------|-----------------|

* Exportacion_Importacion_Ecuador_*xls: Daily energy exports and imports from and to Ecuador (Each file has 1 year data)

	- Not all entries have data

|Fecha|Exportaciones kWh|Importaciones kWh|
|-----|-----------------|-----------------|

* Exportacion_Importacion_Venezuela_*xls: Daily energy exports and imports from and to Venezuela (Each file has 1 year data)

	- Not all entries have data

|Fecha|Exportaciones kWh|Importaciones kWh|
|-----|-----------------|-----------------|

___

### Demanda/Demanda Potencia

* Demanda_Maxima_De_Potencia_*.xlsx: Daily maximum demand (Each file has 1 year data)

|Fecha|Demanda Máxima de Potenca kW|
|-----|----------------------------|

___

### Hidrología

* Aportes_Diario_*.xlsx: Daily contribution of River to the Energy grid (Each file has 1 year data)

|Fecha|Region Hidrologica|Nombre Río|Aportes Caudal m3/s|Aportes Energía kWh|Aportes %|
|-----|------------------|----------|-------------------|-------------------|---------|

* Aportes_Menusal_*.xlsx: Monthly contribution of River to the Energy grid (Each file has 1 year data)

|Año|Mes|Region Hidrologica|Nombre Río|Aportes Energía kWh|Aportes Caudal m3/s|Aportes Media Histórica Energía kWh|Aportes Media Histórica Caudal m3/s|Aportes 95 PSS Energía kWh|Aportes 95 PSS Caudal m3/s|
|---|---|------------------|----------|-------------------|-------------------|-----------------------------------|-----------------------------------|--------------------------|--------------------------|


* Reservas_Diario_*.xls: Daily data on reservoirs (Each file has 1 year data)

|Fecha|Region Hidrologica|Nombre Embalse|Volumen Útil Diario Mm3|Volumen Útil Diario Energía kWh|Volumen Útil Díario %|Volumen Mm3|Volumen Energía kWh|Volumen %|
|-----|------------------|--------------|-----------------------|-------------------------------|---------------------|-----------|-------------------|---------|

* Reservas_Mensual_*.xls: Monthly data on reservoirs (Each file has 1 year data)

|Año|Mes|Region Hidrologica|Nombre Embalse|Capacidad Útil Volumen Mm3|Volumen Máximo Técnico Energía kWh|Capacidad Útil Energía kWh|Volumen Útil Diario Mm3|Volumen Útil Diario Energía kWh|Volumen Útil Diario %|
|---|---|------------------|--------------|--------------------------|----------------------------------|--------------------------|-----------------------|-------------------------------|---------------------|

* Vertimentos_Diario_*.xls: Daily water dumping data (Each file has 1 year data).

|Fecha|Region Hidrologica|Nombre Embalse|Vertimientos Volumen miles m3|Vertimientos Energía kWh|
|-----|------------------|--------------|-----------------------------|------------------------|

___


### Intercambios

* Exportaciones_($)_*.xls: Daily Exports to Ecuador (Money) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Exportaciones_(kWh)_*.xls: Daily Exports to Ecuador (kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Importaciones_($)_*.xls: Daily Imports from Ecuador (Money) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Importaciones_(kWh)_*.xls: Daily Imports from Ecuador (kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|


* Precio_Liquidacion_Exportaciones_($kWh)_*.xls: Daily Price exports to Ecuador ($kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Precio_Liquidacion_Importaciones_($kWh)_($)_*.xls: Daily Price Imports from Ecuador ($kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Precio_Oferta_Colombia_Exportador_($kWh)_*.xls: Daily Price Exports to Ecuador ($kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??
	- What's the difference bewteen this and Precio Liquidacion?

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Precio_Oferta_Pais_Importador_($kWh)_*.xls: Daily Price Imports ??? to Ecuador ($kWh) (Each file has 1 year data, only 2018-2019 are not empty)

	- Enlace??
	- What's this one?

|Fecha|Enlace|0-23|Version|
|-----|------|----|-------|

* Renta_Congestion_Colombia_($)_*.xls: Daily ??? (Not too many data points) (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Renta $|Version|
|-----|-------|-------|

* Renta_Congestion_Destinacion_FOES_($)_*.xls: Daily ??? (Not too many data points) (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Renta $|Version|
|-----|-------|-------|

* Rentas_Congestion_Ecuador_($)_*.xls: Daily ??? (Not too many data points) (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Renta $|Version|
|-----|-------|-------|

* Rentas_Congestion_Para_Cubrir_Restricciones_($)_*.xls: Daily ??? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Código Agente|Renta $|Version|
|-----|-------------|-------|-------|

___

## Oferta

* AGC_Programado_(kWh)_*.xls: ??? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|
|-----|-------|-------------|----|

* Capacidad_Efectiva_Neta_(kW)_*.xls: Efective capacity ?? (Since 2016 is semester data, however only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|Tipo de Generación|Combustible por defecto|Tipo de Despacho|Es Menor|Es Autogenerador|Capacidad Efectiva Neta kW|
|-----|-------|-------------|------------------|-----------------------|----------------|--------|----------------|--------------------------|

* Consumo_De_Combustible_(MBTU)_*.xls: Fuel compsumption (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|Combustible|Consumo Combustible (MBTU)|Version|
|-----|-------|-------------|-----------|--------------------------|-------|

* Disponibilidad_Comercial_(kW)_*.xls: Commercial availability ?? (Since 2016 is semester data, however  only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Disponibilidad_Declarada_(kW)_*.xls: Declared availability ?? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|
|-----|-------|-------------|----|

* Disponibilidad_Ofertada_AGC_(kW)_*.xls: Offered availability ?? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Unidad Generación|Código Agente|0-23|
|-----|-----------------|-------------|----|

* Disponibilidad_Real_(kW)_*.xls: Real availability ?? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Tipo Generación|Código Agente|0-23|
|-----|-------|---------------|-------------|----|

* Disponibilidad_Real_(Porcentaje)_*.xls: Real availability in Percentage (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|
|-----|-------|-------------|----|

* Emisiones de CO2_Historico.xlsx: Empty

* Generacion_de_Seguridad_(kWh)_*.xls: Safety Generation (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Tipo Generación|Código Agente|0-23|Versión|
|-----|-------|---------------|-------------|----|-------|

* Generacion_Ideal_(kWh)_*.xls: Ideal generation (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Generacion_(kWh)_*.xls: Generation(Since 2016 is semester data, however  only 2018-2019 are not empty)

	-	Seems to be the consolidated of most of the files

|Fecha|Recurso|Tipo Generación|Combustible|Código Agente|Tipo Despacho|Es Menor|Es Autogenerador|0-23|Version|
|-----|-------|---------------|-----------|-------------|-------------|--------|----------------|----|-------|

*  Generacion_Programada_(kWh)_*.xls: Programmed generation (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Código Agente|0-23|
|-----|-------|-------------|----|

___

## Transacciones y Precio

* Compras_Bolsa_Internacional_(kWh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Compras_Bolsa_Nacional_(kWh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Compras_Bolsa_TIE_(kWh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Compras_Contrato_(kWh)_*.xlsx|xls:  (Each file has 1 year data).

- Not all have Version

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Costo_Marginal_Despacho_Programado_($kWh)_*.xlsx|xls:  (Each file has 1 year data).

- Not all have Version

|Fecha|0-23|Version|
|-----|----|-------|

* Delta_Internacional_Delta_Nacional_($kWh)_*.xlsx|xls:  (Each file has 1 year data). (Data from 2010-2019)

|Fecha|Delta Internacional|Delta Nacional|Versión|
|-----|-------------------|--------------|-------|

* Desviaciones_(kWh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Maximo_Precio_Oferta_Internacional_($kWh)_*.xlsx|xls:  (Each file has 1 year data). (2009-2019)

	- Not all have Version

|Fecha|0-23|Version|
|-----|----|-------|

* Maximo_Precio_Oferta_Nacional_($kWh)_*.xlsx|xls:  (Each file has 1 year data). (2009-2019)

	- Not all have Version

|Fecha|0-23|Version|
|-----|----|-------|

* Precio_Bolsa_Internacional_($kwh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|0-23|Version|
|-----|----|-------|

* Precio_Bolsa_Nacional_($kwh)_*.xlsx|xls:  (Each file has 1 year data). (1995-2019)

	-	On new files last column is version, old files last column is average

|Fecha|0-23|Version|
|-----|----|-------|

* Precio_Bolsa_Nacional_Ponderado ($kWh)_*.xlsx: 2018-2019

|Fecha|Valor|
|-----|-----|

* Precio_Bolsa_TIE($kwh)_*.xlsx|xls:  (Each file has 1 year data). (2009-2019)

	- Not all have Version

|Fecha|0-23|Version|
|-----|----|-------|

* Precio_Oferta_($kwh)_*.xlsx|xls:  (Each file has 1 year data).

|Fecha|Recurso|Código Agente|Precio de Oferta Ideal $/kWh|Precio de Oferta de Despacho $/kWh|Precio de Oferta Declarado $/kWh|
|-----|-------|-------------|----------------------------|----------------------------------|--------------------------------|

* Precios_Mensuales_($kWh)_*.xlsx|xls: (Each file has 1 year data).

|Año|Mes|Precio Escasez $/kWh|MC  $/kWh|CERE $/kWh|CEE $/kWh|FAZNI Precio $/kWh|Precio Promedio Contrato|Precio Promedio Contratos Regulados|Precio Promedio Contratos No Regulados|
|---|---|--------------------|---------|----------|---------|------------------|------------------------|-----------------------------------|--------------------------------------|

* Reconciliacion_Negativa_AGC_(kWh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Reconciliacion_Negativa_(kwh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Reconciliacion_Positiva_AGC_(kWh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Reconciliacion_Positiva_(kwh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Restriciones_Aliviadas_($)_*.xlsx: 2018-2019

|Fecha|Valor|
|-----|-----|

* Servicio_AGC_(kwh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Recurso|Código Agente|0-23|Version|
|-----|-------|-------------|----|-------|

* Servicios_($)_*.xlsx: (2000-2013)

|Año|Mes|SIC $|CND $|LAC $|Version|
|---|---|-----|-----|-----|-------|

* Ventas_Bolsa_Internacional_(kwh)_*.xlsx|xls: (Each file has 1 year data).

	- There are some files with missing data

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Ventas_Bolsa_Nacional_(kwh)_*.xlsx|xls: (Each file has 1 year data).

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Ventas_Bolsa_TIE_(kwh)_*.xlsx|xls: (Each file has 1 year data). (2009-2019)

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|

* Ventas_Contrato_(kwh)_*.xlsx|xls: (Each file has 1 year data). 

|Fecha|Código Agente|0-23|Version|
|-----|-------------|----|-------|
