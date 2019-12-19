# Data selected for analysis

# XM:

Market data, Interconnected National System (SIN) (All other entities that generate and consume energy outside this system is not included)

### Hydrology

Comprises al hidrology related information

* Aportes_Diario_*.xlsx: Daily contribution of River to the Energy grid (Each file has 1 year data)

|Fecha|Region Hidrologica|Nombre Río|Aportes Caudal m3/s|Aportes Energía kWh|Aportes %|
|-----|------------------|----------|-------------------|-------------------|---------|

* Aportes_Mensual_*.xlsx: Monthly contribution of River to the Energy grid (Each file has 1 year data)

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

### Price & Transaccions

* Precio_Bolsa_Nacional_($kwh)_*.xlsx|xls:  (Each file has 1 year data). (1995-2019)

	-	On new files last column is version, old files last column is average

|Fecha|0-23|Version|
|-----|----|-------|

### Oferta

* Disponibilidad_Real_(kW)_*.xls: Real availability ?? (Each file has 1 year data, only 2018-2019 are not empty)

|Fecha|Recurso|Tipo Generación|Código Agente|0-23|
|-----|-------|---------------|-------------|----|

## NOAA:

Macroclimatic data. Monthly data 20 different indicators ocean-atmospheric e.g. Temperature Pacific Ocean Zone 3-4 etc.

## TRRM/CHIRPS

Estimated precipitation data.

## Geographical Data

- DEM: Digital Elevation Model
- Sources of generation (XM)



