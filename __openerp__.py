# -*- encoding: utf-8 -*-

{
    "name" : "OpenAT ProduktPass Reports",
    "version" : "1.0",
    "description" : """

    Dieses Modul erweitert die Berichtsvorlagen fuer die Lebensmittelindusttrie in form von Speziellen Produktpaessen nach vorgaben des Kunden.

    """,
    "author" : "OpenAT",
    "website" : "http://www.openat.at",
    "url" : "http://www.openat.at",
    "depends" : ['base', 'report_aeroo', 'openat_produktpass', 'product'],
    "init_xml" : [],
    "update_xml" : ['preprocess.xml', 'reports/custom_report_produktpass.xml'],
    "demo_xml" : [],
    "installable" : True,
    "active" : False,
}
