# Bulk Upload (BU)

## BU process
> step-by-step BU procedure from the user-side

To gain some precious minutes on the repeated BU processes, we set up a user protocol for file/folder structure and naming based on current practices.

- choose a short and self-explanatory name for your **BU files**, for example, the name of grid cell-subpart-name (ex: `E61N31-23-Bijan.xlsx`)

- put the BUs worksheet on a **folder** named YYYY-MM-DD-Name (ex: 2021-11-23-Bijan). If you run various BUs processes the same day, you will have to name your folders with different suffixes (ex: 2021-11-22-Bijan, 2021-11-22a-Bijan)

- put these folders on **your** OneDrive, and send a Slack message to the Database Manager with the link to this folder 

- if **the BU does not work**, because there are errors, I will send you an error report in the form of a error JSON file named in the same way as your BU files (ex: [`E61N31-22-Bijan.json`](https://github.com/eamena-oxford/eamena-arches-dev/blob/main/output/bulk/Bulks/2021-11-21-Bijan/E61N31-21-Bijan.json))

- following the recommendations of the error JSON file, you will have to correct the content of your file. Once done, change the name to something explicit, like adding `-rev` at the end of the file name (ex: `E61N31-22-Bijan.xlsx` -> `E61N31-22-Bijan-rev.xlsx`)

- if **the BU works**, I will send you a confirmation, and -- if you ask me to -- we can send you a [BU summary]() in the form of a JSON file named in the same way as your BU files + sum (ex: [`E61N31-22-Bijan-rev-sum.json`](https://github.com/eamena-oxford/eamena-arches-dev/blob/main/output/bulk/Bulks/2021-11-21-Bijan/E61N31-21-Bijan-rev-sum.json))

- once you received the confirmation that your BU has been uploaded into the DB, move your BU sheet into an archives folder 

I have recreated the 'ideal' file/folder naming/structure on the [Bulks/](https://github.com/eamena-oxford/eamena-arches-dev/tree/main/output/bulk/Bulks) folder


## BU summary
> After a BU, render a short summary for the user

Once the BU process complete, a resume can be displayed with a python command[^1]. The result is copied/pasted in a JSON file. A S&R allows to convert the UUID into an URL[^2]


<p align="center">
  <img alt="img-name" src="img/json_summary.png" width="700">
  <br>
    <em>screenshot of the JSON with URL</em>
</p>

The URL opens the Resource Report

<p align="center">
  <img alt="img-name" src="img/json_summary_uuid.png" width="700">
  <br>
    <em>screenshot of the Resource Report</em>
</p>

The Resource name can be search in the map database

<p align="center">
  <img alt="img-name" src="img/json_summary_uuid_search.png" width="700">
  <br>
    <em>screenshot of the Resource Report</em>
</p>


[^1]: `python /opt/arches/eamena/manage.py bu -o summary -s "filename.json" | json_pp`
[^2]: Search: `"uuid" : "`, Replace by `"uuid" : "https://database.eamena.org/en/report/`