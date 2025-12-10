# burgtheater-event-crawler

Repo to store code and data to crawl [https://kulturerbe.burgtheater.at/](https://kulturerbe.burgtheater.at/)

## howto

### list of years
(adapt `year_range = range(1850, 1880)`)
```bash
uv run years.py
```

### list of perfomances
```bash
uv run events.py
```

### list of persons
```bash
uv run persons.py
```


## entrypoints

### list-view by year
https://kulturerbe-import.burgtheater.at/api/api/v1/calendar/1776

### performance-detail-view
https://kulturerbe-import.burgtheater.at/api/api/v1/performance/6671cd3dcd334071f77645a3

### person-detail-view
https://kulturerbe-import.burgtheater.at/api/api/v1/person/6504166ba47588ad6024a95e




## what to do with the data

* enrich persons with GNDs (Werkvertrag)
* import persons to PMB (with Burgtheater URI)
* import events to PMB (with Burgtheater URI)
* link event to
  * persons (the data has roles "authors", "crew" "cast")
  * place/institution (I think it is either Burgtheater or Akademietheater)
  * to work (this is tricky because afaik the works are not modelled in data)
    * check if this is actually true
* call it a day and go for a beer
