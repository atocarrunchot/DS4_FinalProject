--
-- Database creation Script
-- Energyblast project
-- DS4A Colombia  Team 23
-- 


--
--  VIEWS
--

--
-- piv_month_inflow
--

create or replace view piv_month_inflow
as
SELECT fecha,
sum(CASE WHEN region = 'VALLE' THEN aportes END) AS valle,
sum(CASE WHEN region = 'ANTIOQUIA' THEN aportes END) AS antioquia,
sum(CASE WHEN region = 'RIOS ESTIMADOS' THEN aportes END) AS rios_estimados,
sum(CASE WHEN region = 'CARIBE' THEN aportes END) AS caribe,
sum(CASE WHEN region = 'CENTRO' THEN aportes END) AS centro,
sum(CASE WHEN region = 'ORIENTE' THEN aportes END) AS oriente,
sum(CASE WHEN rio = 'EL QUIMBO' THEN aportes END) AS centro$el_quimbo,
sum(CASE WHEN rio = 'FLORIDA II' THEN aportes END) AS valle$florida_ii,
sum(CASE WHEN rio = 'SAN CARLOS' THEN aportes END) AS antioquia$san_carlos,
sum(CASE WHEN rio = 'GUAVIO' THEN aportes END) AS oriente$guavio,
sum(CASE WHEN rio = 'CONCEPCION' THEN aportes END) AS antioquia$concepcion,
sum(CASE WHEN rio = 'GRANDE' THEN aportes END) AS antioquia$grande,
sum(CASE WHEN rio = 'MIEL I' THEN aportes END) AS antioquia$miel_i,
sum(CASE WHEN rio = 'GUATAPE' THEN aportes END) AS antioquia$guatape,
sum(CASE WHEN rio = 'A. SAN LORENZO' THEN aportes END) AS antioquia$a_san_lorenzo,
sum(CASE WHEN rio = 'TENCHE' THEN aportes END) AS antioquia$tenche,
sum(CASE WHEN rio = 'PORCE2 CP' THEN aportes END) AS antioquia$porce2_cp,
sum(CASE WHEN rio = 'BOGOTA N.R.' THEN aportes END) AS centro$bogota_nr,
sum(CASE WHEN rio = 'PRADO' THEN aportes END) AS centro$prado,
sum(CASE WHEN rio = 'CHUZA' THEN aportes END) AS oriente$chuza,
sum(CASE WHEN rio = 'BATA' THEN aportes END) AS oriente$bata,
sum(CASE WHEN rio = 'DESV. EEPPM (NEC,PAJ,DOL)' THEN aportes END) AS antioquia$desv_eeppm_necpajdol,
sum(CASE WHEN rio = 'DESV. GUARINO' THEN aportes END) AS antioquia$desv_guarino,
sum(CASE WHEN rio = 'MAGDALENA BETANIA' THEN aportes END) AS centro$magdalena_betania,
sum(CASE WHEN rio = 'BETANIA CP' THEN aportes END) AS centro$betania_cp,
sum(CASE WHEN rio = 'GUADALUPE' THEN aportes END) AS antioquia$guadalupe,
sum(CASE WHEN rio = 'DESV. MANSO' THEN aportes END) AS antioquia$desv_manso,
sum(CASE WHEN rio = 'PORCE III' THEN aportes END) AS antioquia$porce_iii,
sum(CASE WHEN rio = 'PORCE II' THEN aportes END) AS antioquia$porce_ii,
sum(CASE WHEN rio = 'OTROS RIOS (ESTIMADOS)' THEN aportes END) AS rios_estimados$otros_rios_estimados,
sum(CASE WHEN rio = 'CARLOS LLERAS' THEN aportes END) AS antioquia$carlos_lleras,
sum(CASE WHEN rio = 'SINU URRA' THEN aportes END) AS caribe$sinu_urra,
sum(CASE WHEN rio = 'CALIMA' THEN aportes END) AS valle$calima,
sum(CASE WHEN rio = 'CAUCA SALVAJINA' THEN aportes END) AS valle$cauca_salvajina,
sum(CASE WHEN rio = 'SOGAMOSO' THEN aportes END) AS centro$sogamoso,
sum(CASE WHEN rio = 'DIGUA' THEN aportes END) AS valle$digua,
sum(CASE WHEN rio = 'AMOYA' THEN aportes END) AS centro$amoya,
sum(CASE WHEN rio = 'ALTOANCHICAYA' THEN aportes END) AS valle$altoanchicaya,
sum(CASE WHEN rio = 'DESV. SAN MARCOS' THEN aportes END) AS centro$desv_san_marcos,
sum(CASE WHEN rio = 'NARE' THEN aportes END) AS antioquia$nare,
sum(CASE WHEN rio = 'CUCUANA' THEN aportes END) AS centro$cucuana
FROM month_inflow
GROUP BY fecha
order by fecha;



--
-- pivot month_offer
--

create view piv_month_offer
as
select fecha,
sum(CASE WHEN region = 'VALLE' THEN oferta END) AS valle,
sum(CASE WHEN region = 'ANTIOQUIA' THEN oferta END) AS antioquia,
sum(CASE WHEN region = 'RIOS ESTIMADOS' THEN oferta END) AS rios_estimados,
sum(CASE WHEN region = 'CARIBE' THEN oferta END) AS caribe,
sum(CASE WHEN region = 'CENTRO' THEN oferta END) AS centro,
sum(CASE WHEN region = 'ORIENTE' THEN oferta END) AS oriente,
sum(CASE WHEN recurso = 'ESMERALDA' THEN oferta END) AS antioquia$esmeralda,
sum(CASE WHEN recurso = 'OCOA 1' THEN oferta END) AS oriente$ocoa_1,
sum(CASE WHEN recurso = 'TERMOCANDELARIA 2' THEN oferta END) AS caribe$termocandelaria_2,
sum(CASE WHEN recurso = 'GUAVIO' THEN oferta END) AS oriente$guavio,
sum(CASE WHEN recurso = 'BARRANQUILLA 3' THEN oferta END) AS caribe$barranquilla_3,
sum(CASE WHEN recurso = 'GUAJIRA 1' THEN oferta END) AS caribe$guajira_1,
sum(CASE WHEN recurso = 'GECELCA 32' THEN oferta END) AS caribe$gecelca_32,
sum(CASE WHEN recurso = 'TASAJERO 1' THEN oferta END) AS caribe$tasajero_1,
sum(CASE WHEN recurso = 'CARTAGENA 3' THEN oferta END) AS caribe$cartagena_3,
sum(CASE WHEN recurso = 'BARRANCA 5' THEN oferta END) AS centro$barranca_5,
sum(CASE WHEN recurso = 'PAIPA 3' THEN oferta END) AS centro$paipa_3,
sum(CASE WHEN recurso = 'PORCE II' THEN oferta END) AS antioquia$porce_ii,
sum(CASE WHEN recurso = 'ZIPAEMG 5' THEN oferta END) AS centro$zipaemg_5,
sum(CASE WHEN recurso = 'PAIPA 4' THEN oferta END) AS centro$paipa_4,
sum(CASE WHEN recurso = 'RIOGRANDE I' THEN oferta END) AS antioquia$riogrande_i,
sum(CASE WHEN recurso = 'FLORES 2' THEN oferta END) AS caribe$flores_2,
sum(CASE WHEN recurso = 'LA TASAJERA' THEN oferta END) AS antioquia$la_tasajera,
sum(CASE WHEN recurso = 'AUTOG ARGOS CARTAGENA' THEN oferta END) AS caribe$autog_argos_cartagena,
sum(CASE WHEN recurso = 'TASAJERO 2' THEN oferta END) AS caribe$tasajero_2,
sum(CASE WHEN recurso = 'BAJO ANCHICAYA' THEN oferta END) AS valle$bajo_anchicaya,
sum(CASE WHEN recurso = 'FLORIDA' THEN oferta END) AS valle$florida,
sum(CASE WHEN recurso = 'ZIPAEMG 4' THEN oferta END) AS centro$zipaemg_4,
sum(CASE WHEN recurso = 'LA HERRADURA' THEN oferta END) AS antioquia$la_herradura,
sum(CASE WHEN recurso = 'SAN CARLOS' THEN oferta END) AS antioquia$san_carlos,
sum(CASE WHEN recurso = 'ZIPAEMG 3' THEN oferta END) AS centro$zipaemg_3,
sum(CASE WHEN recurso = 'AUTOG REFICAR' THEN oferta END) AS caribe$autog_reficar,
sum(CASE WHEN recurso = 'TERMOEMCALI 1' THEN oferta END) AS valle$termoemcali_1,
sum(CASE WHEN recurso = 'GUATAPE' THEN oferta END) AS antioquia$guatape,
sum(CASE WHEN recurso = 'FLORES 3' THEN oferta END) AS caribe$flores_3,
sum(CASE WHEN recurso = 'MERILECTRICA 1' THEN oferta END) AS centro$merilectrica_1,
sum(CASE WHEN recurso = 'SAN FRANCISCO' THEN oferta END) AS antioquia$san_francisco,
sum(CASE WHEN recurso = 'TERMOVALLE 1' THEN oferta END) AS valle$termovalle_1,
sum(CASE WHEN recurso = 'EL PASO' THEN oferta END) AS caribe$el_paso,
sum(CASE WHEN recurso = 'DARIO VALENCIA' THEN oferta END) AS centro$dario_valencia,
sum(CASE WHEN recurso = 'TERMOYOPAL 1' THEN oferta END) AS oriente$termoyopal_1,
sum(CASE WHEN recurso = 'AUTOG COCA-COLA FEMSA' THEN oferta END) AS valle$autog_cocacola_femsa,
sum(CASE WHEN recurso = 'DARIO VALENCIA SAMPER' THEN oferta END) AS centro$dario_valencia_samper,
sum(CASE WHEN recurso = 'CARLOS LLERAS' THEN oferta END) AS antioquia$carlos_lleras,
sum(CASE WHEN recurso = 'BARRANCA 2' THEN oferta END) AS centro$barranca_2,
sum(CASE WHEN recurso = 'GUAJIRA 2' THEN oferta END) AS caribe$guajira_2,
sum(CASE WHEN recurso = 'PAGUA' THEN oferta END) AS centro$pagua,
sum(CASE WHEN recurso = 'FLORES 1' THEN oferta END) AS caribe$flores_1,
sum(CASE WHEN recurso = 'AUTOG ARGOS YUMBO' THEN oferta END) AS valle$autog_argos_yumbo,
sum(CASE WHEN recurso = 'MIEL I' THEN oferta END) AS antioquia$miel_i,
sum(CASE WHEN recurso = 'BARRANCA 4' THEN oferta END) AS centro$barranca_4,
sum(CASE WHEN recurso = 'EL MORRO 1' THEN oferta END) AS oriente$el_morro_1,
sum(CASE WHEN recurso = 'URRA' THEN oferta END) AS caribe$urra,
sum(CASE WHEN recurso = 'TEBSAB' THEN oferta END) AS caribe$tebsab,
sum(CASE WHEN recurso = 'TERMOYOPAL 2' THEN oferta END) AS oriente$termoyopal_2,
sum(CASE WHEN recurso = 'CARTAGENA 2' THEN oferta END) AS caribe$cartagena_2,
sum(CASE WHEN recurso = 'BARRANQUILLA 4' THEN oferta END) AS caribe$barranquilla_4,
sum(CASE WHEN recurso = 'BARRANCA 3' THEN oferta END) AS centro$barranca_3,
sum(CASE WHEN recurso = 'CHIVOR' THEN oferta END) AS oriente$chivor,
sum(CASE WHEN recurso = 'SALVAJINA' THEN oferta END) AS valle$salvajina,
sum(CASE WHEN recurso = 'ALBAN' THEN oferta END) AS valle$alban,
sum(CASE WHEN recurso = 'PLAYAS' THEN oferta END) AS antioquia$playas,
sum(CASE WHEN recurso = 'AMOYA' THEN oferta END) AS centro$amoya,
sum(CASE WHEN recurso = 'BETANIA' THEN oferta END) AS centro$betania,
sum(CASE WHEN recurso = 'CIMARRON' THEN oferta END) AS oriente$cimarron,
sum(CASE WHEN recurso = 'PROELECTRICA 1' THEN oferta END) AS caribe$proelectrica_1,
sum(CASE WHEN recurso = 'CASALCO' THEN oferta END) AS centro$casalco,
sum(CASE WHEN recurso = 'PROELECTRICA 2' THEN oferta END) AS caribe$proelectrica_2,
sum(CASE WHEN recurso = 'TERMODORADA 1' THEN oferta END) AS antioquia$termodorada_1,
sum(CASE WHEN recurso = 'PAIPA 1' THEN oferta END) AS centro$paipa_1,
sum(CASE WHEN recurso = 'JAGUAS' THEN oferta END) AS antioquia$jaguas,
sum(CASE WHEN recurso = 'GECELCA 3' THEN oferta END) AS caribe$gecelca_3,
sum(CASE WHEN recurso = 'EL QUIMBO' THEN oferta END) AS centro$el_quimbo,
sum(CASE WHEN recurso = 'AUTOG FAMILIA' THEN oferta END) AS centro$autog_familia,
sum(CASE WHEN recurso = 'AUTOG UNIBOL' THEN oferta END) AS caribe$autog_unibol,
sum(CASE WHEN recurso = 'GUATRON' THEN oferta END) AS antioquia$guatron,
sum(CASE WHEN recurso = 'TERMOSIERRAB' THEN oferta END) AS antioquia$termosierrab,
sum(CASE WHEN recurso = 'PAIPA 2' THEN oferta END) AS centro$paipa_2,
sum(CASE WHEN recurso = 'TERMONORTE' THEN oferta END) AS caribe$termonorte,
sum(CASE WHEN recurso = 'TERMOSIERRA 2' THEN oferta END) AS antioquia$termosierra_2,
sum(CASE WHEN recurso = 'FLORES 4B' THEN oferta END) AS caribe$flores_4b,
sum(CASE WHEN recurso = 'AMOYA LA ESPERANZA' THEN oferta END) AS centro$amoya_la_esperanza,
sum(CASE WHEN recurso = 'RIO MAYO' THEN oferta END) AS valle$rio_mayo,
sum(CASE WHEN recurso = 'SAN MIGUEL' THEN oferta END) AS antioquia$san_miguel,
sum(CASE WHEN recurso = 'SALTO II' THEN oferta END) AS centro$salto_ii,
sum(CASE WHEN recurso = 'PRADO' THEN oferta END) AS centro$prado,
sum(CASE WHEN recurso = 'YUMBO 3' THEN oferta END) AS valle$yumbo_3,
sum(CASE WHEN recurso = 'CARTAGENA 1' THEN oferta END) AS caribe$cartagena_1,
sum(CASE WHEN recurso = 'PALENQUE 3' THEN oferta END) AS centro$palenque_3,
sum(CASE WHEN recurso = 'AUTOG YAGUARITO' THEN oferta END) AS valle$autog_yaguarito,
sum(CASE WHEN recurso = 'TERMOCENTRO CC' THEN oferta END) AS centro$termocentro_cc,
sum(CASE WHEN recurso = 'PORCE III' THEN oferta END) AS antioquia$porce_iii,
sum(CASE WHEN recurso = 'BARRANCA 1' THEN oferta END) AS centro$barranca_1,
sum(CASE WHEN recurso = 'CALIMA' THEN oferta END) AS valle$calima,
sum(CASE WHEN recurso = 'EL POPAL' THEN oferta END) AS antioquia$el_popal,
sum(CASE WHEN recurso = 'ZIPAEMG 2' THEN oferta END) AS centro$zipaemg_2,
sum(CASE WHEN recurso = 'SOGAMOSO' THEN oferta END) AS centro$sogamoso,
sum(CASE WHEN recurso = 'TERMOCANDELARIA 1' THEN oferta END) AS caribe$termocandelaria_1,
sum(CASE WHEN recurso = 'AUTOG ARGOS SOGAMOSO' THEN oferta END) AS centro$autog_argos_sogamoso,
sum(CASE WHEN recurso = 'CUCUANA' THEN oferta END) AS centro$cucuana
FROM month_offer
GROUP BY fecha
ORDER BY fecha
;

--
-- month_precipitation
--


create view piv_month_precipitation
as
select fecha,
avg(CASE WHEN region = 'Caribe' THEN precipitacion END) AS caribe,
avg(CASE WHEN region = 'Valle' THEN precipitacion END) AS valle,
avg(CASE WHEN region = 'Oriente' THEN precipitacion END) AS oriente,
avg(CASE WHEN region = 'Centro' THEN precipitacion END) AS centro,
avg(CASE WHEN region = 'Antioquia' THEN precipitacion END) AS antioquia,
avg(CASE WHEN recurso = 'Porce III' THEN precipitacion END) AS antioquia$porce_iii,
avg(CASE WHEN recurso = 'Jaguas' THEN precipitacion END) AS antioquia$jaguas,
avg(CASE WHEN recurso = 'Pagua' THEN precipitacion END) AS centro$pagua,
avg(CASE WHEN recurso = 'San Carlos' THEN precipitacion END) AS antioquia$san_carlos,
avg(CASE WHEN recurso = 'La Tasajera' THEN precipitacion END) AS antioquia$la_tasajera,
avg(CASE WHEN recurso = 'Calima' THEN precipitacion END) AS valle$calima,
avg(CASE WHEN recurso = 'Chivor' THEN precipitacion END) AS oriente$chivor,
avg(CASE WHEN recurso = 'Guatape' THEN precipitacion END) AS antioquia$guatape,
avg(CASE WHEN recurso = 'Porce II' THEN precipitacion END) AS antioquia$porce_ii,
avg(CASE WHEN recurso = 'Playas' THEN precipitacion END) AS antioquia$playas,
avg(CASE WHEN recurso = 'Guavio' THEN precipitacion END) AS oriente$guavio,
avg(CASE WHEN recurso = 'Sogamoso' THEN precipitacion END) AS centro$sogamoso,
avg(CASE WHEN recurso = 'Quimbo' THEN precipitacion END) AS centro$quimbo,
avg(CASE WHEN recurso = 'Salvajina' THEN precipitacion END) AS valle$salvajina,
avg(CASE WHEN recurso = 'Betania' THEN precipitacion END) AS centro$betania,
avg(CASE WHEN recurso = 'Guatron' THEN precipitacion END) AS antioquia$guatron,
avg(CASE WHEN recurso = 'Prado' THEN precipitacion END) AS centro$prado,
avg(CASE WHEN recurso = 'Urra' THEN precipitacion END) AS caribe$urra,
avg(CASE WHEN recurso = 'Miel I' THEN precipitacion END) AS antioquia$miel_i,
avg(CASE WHEN recurso = 'Alban' THEN precipitacion END) AS valle$alban,
sum(CASE WHEN embalse = 'Porce III' THEN precipitacion END) AS antioquia$porce_iii$porce_iii,
sum(CASE WHEN embalse = 'San Lorenzo' THEN precipitacion END) AS antioquia$jaguas$san_lorenzo,
sum(CASE WHEN embalse = 'Chuza' THEN precipitacion END) AS centro$pagua$chuza,
sum(CASE WHEN embalse = 'Punchina' THEN precipitacion END) AS antioquia$san_carlos$punchina,
sum(CASE WHEN embalse = 'Riogrande2' THEN precipitacion END) AS antioquia$la_tasajera$riogrande2,
sum(CASE WHEN embalse = 'Porce III CP' THEN precipitacion END) AS antioquia$porce_iii$porce_iii_cp,
sum(CASE WHEN embalse = 'Calima 1' THEN precipitacion END) AS valle$calima$calima_1,
sum(CASE WHEN embalse = 'Esmeralda' THEN precipitacion END) AS oriente$chivor$esmeralda,
sum(CASE WHEN embalse = 'Punchina CP' THEN precipitacion END) AS antioquia$san_carlos$punchina_cp,
sum(CASE WHEN embalse = 'Penol' THEN precipitacion END) AS antioquia$guatape$penol,
sum(CASE WHEN embalse = 'Porce II CP' THEN precipitacion END) AS antioquia$porce_ii$porce_ii_cp,
sum(CASE WHEN embalse = 'Playas CP' THEN precipitacion END) AS antioquia$playas$playas_cp,
sum(CASE WHEN embalse = 'Guavio' THEN precipitacion END) AS oriente$guavio$guavio,
sum(CASE WHEN embalse = 'Porce II' THEN precipitacion END) AS antioquia$porce_ii$porce_ii,
sum(CASE WHEN embalse = 'Topocoro' THEN precipitacion END) AS centro$sogamoso$topocoro,
sum(CASE WHEN embalse = 'Quimbo' THEN precipitacion END) AS centro$quimbo$quimbo,
sum(CASE WHEN embalse = 'Salvajina' THEN precipitacion END) AS valle$salvajina$salvajina,
sum(CASE WHEN embalse = 'Tomine' THEN precipitacion END) AS centro$pagua$tomine,
sum(CASE WHEN embalse = 'Betania' THEN precipitacion END) AS centro$betania$betania,
sum(CASE WHEN embalse = 'Betania CP' THEN precipitacion END) AS centro$betania$betania_cp,
sum(CASE WHEN embalse = 'Troneras' THEN precipitacion END) AS antioquia$guatron$troneras,
sum(CASE WHEN embalse = 'Prado' THEN precipitacion END) AS centro$prado$prado,
sum(CASE WHEN embalse = 'San Lorenzo CP' THEN precipitacion END) AS antioquia$jaguas$san_lorenzo_cp,
sum(CASE WHEN embalse = 'Urra1' THEN precipitacion END) AS caribe$urra$urra1,
sum(CASE WHEN embalse = 'Amani' THEN precipitacion END) AS antioquia$miel_i$amani,
sum(CASE WHEN embalse = 'Miraflores' THEN precipitacion END) AS antioquia$guatron$miraflores,
sum(CASE WHEN embalse = 'Sisga' THEN precipitacion END) AS centro$pagua$sisga,
sum(CASE WHEN embalse = 'Muna' THEN precipitacion END) AS centro$pagua$muna,
sum(CASE WHEN embalse = 'Altoanchicaya' THEN precipitacion END) AS valle$alban$altoanchicaya,
sum(CASE WHEN embalse = 'Playas' THEN precipitacion END) AS antioquia$playas$playas,
sum(CASE WHEN embalse = 'Neusa' THEN precipitacion END) AS centro$pagua$neusa
FROM month_precipitation
GROUP BY fecha
ORDER BY fecha
;


--
-- piv_month_spill
--



create view piv_month_spill
as
select fecha,
sum(CASE WHEN region = 'VALLE' THEN vertimiento END) AS valle,
sum(CASE WHEN region = 'ANTIOQUIA' THEN vertimiento END) AS antioquia,
sum(CASE WHEN region = 'CARIBE' THEN vertimiento END) AS caribe,
sum(CASE WHEN region = 'CENTRO' THEN vertimiento END) AS centro,
sum(CASE WHEN region = 'ORIENTE' THEN vertimiento END) AS oriente,
sum(CASE WHEN embalse = 'ESMERALDA' THEN vertimiento END) AS oriente$esmeralda,
sum(CASE WHEN embalse = 'AGREGADO BOGOTA' THEN vertimiento END) AS centro$agregado_bogota,
sum(CASE WHEN embalse = 'EL QUIMBO' THEN vertimiento END) AS centro$el_quimbo,
sum(CASE WHEN embalse = 'PUNCHINA' THEN vertimiento END) AS antioquia$punchina,
sum(CASE WHEN embalse = 'GUAVIO' THEN vertimiento END) AS oriente$guavio,
sum(CASE WHEN embalse = 'PENOL' THEN vertimiento END) AS antioquia$penol,
sum(CASE WHEN embalse = 'URRA1' THEN vertimiento END) AS caribe$urra1,
sum(CASE WHEN embalse = 'MIEL I' THEN vertimiento END) AS antioquia$miel_i,
sum(CASE WHEN embalse = 'SALVAJINA' THEN vertimiento END) AS valle$salvajina,
sum(CASE WHEN embalse = 'TOPOCORO' THEN vertimiento END) AS centro$topocoro,
sum(CASE WHEN embalse = 'RIOGRANDE2' THEN vertimiento END) AS antioquia$riogrande2,
sum(CASE WHEN embalse = 'CALIMA1' THEN vertimiento END) AS valle$calima1,
sum(CASE WHEN embalse = 'PLAYAS' THEN vertimiento END) AS antioquia$playas,
sum(CASE WHEN embalse = 'AMANI' THEN vertimiento END) AS antioquia$amani,
sum(CASE WHEN embalse = 'ALTOANCHICAYA' THEN vertimiento END) AS valle$altoanchicaya,
sum(CASE WHEN embalse = 'BETANIA' THEN vertimiento END) AS centro$betania,
sum(CASE WHEN embalse = 'SAN LORENZO' THEN vertimiento END) AS antioquia$san_lorenzo,
sum(CASE WHEN embalse = 'PRADO' THEN vertimiento END) AS centro$prado,
sum(CASE WHEN embalse = 'CHUZA' THEN vertimiento END) AS oriente$chuza,
sum(CASE WHEN embalse = 'TRONERAS' THEN vertimiento END) AS antioquia$troneras,
sum(CASE WHEN embalse = 'PORCE III' THEN vertimiento END) AS antioquia$porce_iii,
sum(CASE WHEN embalse = 'PORCE II' THEN vertimiento END) AS antioquia$porce_ii
from month_spill
group by fecha
order by fecha;


--
-- piv_month_storage
--

create or replace view piv_month_storage
as
select fecha,
sum(CASE WHEN region = 'VALLE' THEN vol_util END) AS valle,
sum(CASE WHEN region = 'ANTIOQUIA' THEN vol_util END) AS antioquia,
sum(CASE WHEN region = 'CARIBE' THEN vol_util END) AS caribe,
sum(CASE WHEN region = 'CENTRO' THEN vol_util END) AS centro,
sum(CASE WHEN region = 'ORIENTE' THEN vol_util END) AS oriente,
sum(CASE WHEN embalse = 'ESMERALDA' THEN vol_util END) AS oriente$esmeralda,
sum(CASE WHEN embalse = 'AGREGADO BOGOTA' THEN vol_util END) AS centro$agregado_bogota,
sum(CASE WHEN embalse = 'EL QUIMBO' THEN vol_util END) AS centro$el_quimbo,
sum(CASE WHEN embalse = 'PUNCHINA' THEN vol_util END) AS antioquia$punchina,
sum(CASE WHEN embalse = 'MIRAFLORES' THEN vol_util END) AS antioquia$miraflores,
sum(CASE WHEN embalse = 'GUAVIO' THEN vol_util END) AS oriente$guavio,
sum(CASE WHEN embalse = 'PENOL' THEN vol_util END) AS antioquia$penol,
sum(CASE WHEN embalse = 'URRA1' THEN vol_util END) AS caribe$urra1,
sum(CASE WHEN embalse = 'SALVAJINA' THEN vol_util END) AS valle$salvajina,
sum(CASE WHEN embalse = 'TOPOCORO' THEN vol_util END) AS centro$topocoro,
sum(CASE WHEN embalse = 'RIOGRANDE2' THEN vol_util END) AS antioquia$riogrande2,
sum(CASE WHEN embalse = 'CALIMA1' THEN vol_util END) AS valle$calima1,
sum(CASE WHEN embalse = 'PLAYAS' THEN vol_util END) AS antioquia$playas,
sum(CASE WHEN embalse = 'AMANI' THEN vol_util END) AS antioquia$amani,
sum(CASE WHEN embalse = 'ALTOANCHICAYA' THEN vol_util END) AS valle$altoanchicaya,
sum(CASE WHEN embalse = 'MUNA' THEN vol_util END) AS centro$muna,
sum(CASE WHEN embalse = 'BETANIA' THEN vol_util END) AS centro$betania,
sum(CASE WHEN embalse = 'SAN LORENZO' THEN vol_util END) AS antioquia$san_lorenzo,
sum(CASE WHEN embalse = 'PRADO' THEN vol_util END) AS centro$prado,
sum(CASE WHEN embalse = 'CHUZA' THEN vol_util END) AS oriente$chuza,
sum(CASE WHEN embalse = 'TRONERAS' THEN vol_util END) AS antioquia$troneras,
sum(CASE WHEN embalse = 'PORCE III' THEN vol_util END) AS antioquia$porce_iii,
sum(CASE WHEN embalse = 'PORCE II' THEN vol_util END) AS antioquia$porce_ii
from month_storage
group by fecha
order by fecha;

