import os
import psycopg2
import json
import csv
import time

ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

print(ELEPHANT_HOST)

dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)

def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    # saformatē pieslēgšanās parametrus
    # dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    # izveido pieslēgumu
    conn = psycopg2.connect(dsn)
    # izveido kursoru
    cur = conn.cursor()
    # aizsūta kursoram SQL vaicājumu
    cur.execute("SELECT version();")
    # pieprasa no kursora atbildi
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    # aizver kursoru
    cur.close()
    # aizver peislēgumu daubāzei
    conn.close()
    return result


def nolasit(parametri = 0):
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    if parametri==0:
        querry='''SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY nrpk ASC'''
    elif parametri.izvele == 1:
        numurs = int(parametri.teksts)
        querry = '''SELECT * FROM (SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY nrpk ASC) AS tabula WHERE tabula.nrpk='{}' '''.format(numurs)
    elif parametri.izvele == 3:
        querry='''SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY nrpk ASC'''
    elif parametri.izvele == 4:
        querry='''SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY uzvards ASC'''
    elif parametri.izvele == 5:
        querry='''SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY nosaukums ASC'''
    elif parametri.izvele == 6:
        querry='''SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY padzilinatie1 ASC, padzilinatie2 ASC, padzilinatie3 ASC'''
    else:
        querry = '''SELECT * FROM (SELECT izvele.nrpk, INITCAP(izvele.vards) as vards, INITCAP(izvele.uzvards) as uzvards, grozi.nosaukums, parastie2.kurss valoda2, parastie3.kurss valoda3, datori.datoru_nosaukums, padzilinatie1.padzkurss padzkurss1, padzilinatie2.padzkurss padzkurss2, padzilinatie3.padzkurss padzkurss3, izvele.specdebates, izvele.specanglit, izvele.specfiloz, izvele.specpub, izvele.specpapangv, izvele.specpsih, izvele.specrobo, izvele.speckrv FROM izvele LEFT JOIN grozi ON izvele.izvele_id=grozi.id LEFT JOIN datori ON izvele.datori_id=datori.id LEFT JOIN padzilinatie AS padzilinatie1 ON padz_id1=padzilinatie1.id LEFT JOIN padzilinatie AS padzilinatie2 ON padz_id2=padzilinatie2.id LEFT JOIN padzilinatie AS padzilinatie3 ON padz_id3=padzilinatie3.id LEFT JOIN parastiekursi AS parastie2 ON otra_valoda=parastie2.id LEFT JOIN parastiekursi AS parastie3 ON tresa_valoda=parastie3.id ORDER BY nrpk ASC) AS tabula WHERE tabula.uzvards LIKE INITCAP('{}%') '''.format(parametri.teksts)
    cur.execute(querry)
    r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return r
