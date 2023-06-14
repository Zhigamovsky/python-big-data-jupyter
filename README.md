# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн

1. South Sudan
2. Mexico
3. China

є наступні матеріали.

## Кодова база

### Python code

- [convert.py](samples/convert.py)

### Jupiter Notebook

- [sample.ipynb](samples/sample.ipynb)


#### Scripts

- [setup-venv.sh](setup-venv.sh)
- [bash start-docker-cli-zhigamovsky-jupyter.sh](start-docker-cli-zhigamovsky-jupyter.sh)
- [bash start-docker-compose-zhigamovsky-jupiter.sh](start-docker-compose-zhigamovsky-jupiter.sh)


### Інші Файли

V1 - Для розгортання середовища Jupiter Notebook через Visual Studio Code у docker | docker_compose:
- [docker-compose.yml](docker-compose.yml)
- [Dockerfile.zhigamovsky_python_jupyter](Dockerfile.zhigamovsky_python_jupyter)
- [requirements.txt](requirements.txt)

V2 - Для розгортання середовища Jupiter Notebook всередині Visual Studio Code у docker | docker_compose:
- [devcontainer.json](.devcontainer/devcontainer.json)
- [requirements.txt](requirements.txt)
- [pyenv.cfg](.venv/pyenv.cfg)
- [kernel.json](.venv/share/jupyter/kernels/python3/kernel.json)

### Extensions

Розширення, які використовував у Visual Studio Code, щоб працювати з Jupyter Notebooks, Python та підняти Docker контейнер
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Jupyter Keymap](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-keymap)
- [Remote - Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server)
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Jupyter Cell Tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
- [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow)
- [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)



### Вхідні дані (разархівовані та сконвертовані дані)

- [oil-prices.zip](datasets/oil-prices.zip)
- [population.zip](datasets/population.zip)
- [ppp.zip](datasets/ppp.zip)


##### file *brent-daily.***

- CSV: [brent-daily.csv](src/oil-prices/brent-daily.csv)
- JSON: [brent-daily.json](src/oil-prices/brent-daily.json)
- XLSX: [brent-daily.xlsx](src/oil-prices/brent-daily_pandas.xlsx)


##### file *population.***

- CSV: [population.csv](src/population/population.csv)
- JSON: [population.json](src/population/population.json)
- XLSX: [population_pandas.xlsx](src/population/population_pandas.xlsx)

##### file *ppp-gdp.***

- CSV: [ppp-gdp.csv](src/ppp/ppp-gdp.csv)
- JSON: [ppp-gdp.json](src/ppp/ppp-gdp.json)
- XLSX: [ppp-gdp_pandas.xlsx](src/ppp/ppp-gdp_pandas.xlsx)

#### Сгенеровані нові дані

##### table *data_population_1960_2020.***

- CSV: [data_population_1960_2020.csv](samples/tables_and_graphs/data_population_1960_2020.csv)
- JSON: [data_population_1960_2020.json](samples/tables_and_graphs/data_population_1960_2020.json)
- XLSX: [data_population_1960_2020.xlsx](samples/tables_and_graphs/data_population_1960_2020.xlsx)

##### table *statistics_population.***

- CSV: [statistics_population.csv](samples/tables_and_graphs/statistics_population.csv)
- JSON: [statistics_population.json](samples/tables_and_graphs/statistics_population.json)
- XLSX: [statistics_population.xlsx](samples/tables_and_graphs/statistics_population.xlsx)

##### table *statistics_ppp.***

- CSV: [statistics_ppp.csv](samples/tables_and_graphs/statistics_ppp.csv)
- JSON: [statistics_ppp.json](samples/tables_and_graphs/statistics_ppp.json)
- XLSX: [statistics_ppp.xlsx](samples/tables_and_graphs/statistics_ppp.xlsx)

##### table *statistics_oil.***

- CSV: [statistics_oil.csv](samples/tables_and_graphs/statistics_oil.csv)
- JSON: [statistics_oil.json](samples/tables_and_graphs/statistics_oil.json)
- XLSX: [statistics_oil.xlsx](samples/tables_and_graphs/statistics_oil.xlsx)

##### table *correlation_oil_ppp.***

- CSV: [correlation_oil_ppp.csv](samples/tables_and_graphs/correlation_oil_ppp.csv)
- JSON: [correlation_oil_ppp.json](samples/tables_and_graphs/correlation_oil_ppp.json)
- XLSX: [correlation_oil_ppp.xlsx](samples/tables_and_graphs/correlation_oil_ppp.xlsx)

##### table *df_percentage_ppp.***

- CSV: [df_percentage_ppp.csv](samples/tables_and_graphs/df_percentage_ppp.csv)
- JSON: [df_percentage_ppp.json](samples/tables_and_graphs/df_percentage_ppp.json)
- XLSX: [df_percentage_ppp.xlsx](samples/tables_and_graphs/df_percentage_ppp.xlsx)

##### table *correlation_population_ppp.***

- CSV: [correlation_population_ppp.csv](samples/tables_and_graphs/correlation_population_ppp.csv)
- JSON: [correlation_population_ppp.json](samples/tables_and_graphs/correlation_population_ppp.json)
- XLSX: [correlation_population_ppp.xlsx](samples/tables_and_graphs/correlation_population_ppp.xlsx)

##### table *correlation_population_oil.***

- CSV: [correlation_population_oil.csv](samples/tables_and_graphs/correlation_population_oil.csv)
- JSON: [correlation_population_oil.json](samples/tables_and_graphs/correlation_population_oil.json)
- XLSX: [correlation_population_oil.xlsx](samples/tables_and_graphs/correlation_population_oil.xlsx)


#### Графіки
- [line1_population.png](samples/tables_and_graphs/line1_population.png)
- [line2_population.png](samples/tables_and_graphs/line2_population.png)
- [line2_population.jpg](samples/tables_and_graphs/line2_population.jpg)
- [line2_population.pdf](samples/tables_and_graphs/line2_population.pdf)
- [pie_population.png](samples/tables_and_graphs/pie_population.png)
- [bar_population.png](samples/tables_and_graphs/bar_population.png)

---

## Інструкція до роботи

У випадку, якщо ви хочете запустити Jupyter Notebook через Visual Studio Code та працювати з Python та мати можливість запускати контейнери у Docker, ви повинні встановити ці розширення для VS Code:

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Jupyter Keymap](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-keymap)
- [Remote - Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server)
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Jupyter Cell Tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
- [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow)
- [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)

1. Запускаемо [convert.py](samples/convert.py).

2. Результат convert.py:
    1. Розпаковка .zip архівів у директорію[data](data/).
    2. Копіювання необхідних файлів з даними у директорію [src](src/).
    3. Конвертування csv-файлів у формати .json та .xlsx.

3. Підіймаємо Docker контейнер
    * (У моєму випадку) Налаштовуємо контейнер Docker віддаленої розробки Visual Studio Code для роботи з Jupyter Lab Notebooks
    * (Або) Запускаємо `bash start-docker-cli-zhigamovsky-jupyter.sh`

4. Виконуємо код [sample.ipynb](samples/sample.ipynb) в Jupiter Notebook (або у моєму випадку через Visual Studio Code у Jupyter Notebook)

5. Результат [sample.ipynb](samples/sample.ipynb)
    1. Створює табличку "Популяції за інтервал часу 1960-2020" за відповідним варіантом у 3-х форматах:
       * [data_population_1960_2020.csv](samples/tables_and_graphs/data_population_1960_2020.csv)
       * [data_population_1960_2020.json](samples/tables_and_graphs/data_population_1960_2020.json)
       * [data_population_1960_2020.xlsx](samples/tables_and_graphs/data_population_1960_2020.xlsx)
    2. Графічно відображає дані з таблички п.1 у 3-х стилях: лінійний, секторний та гістограмний.
       Зокрема:
        * [line1_population.png](samples/tables_and_graphs/line1_population.png)
        * [line2_population.png](samples/tables_and_graphs/line2_population.png)
        * [pie_population.png](samples/tables_and_graphs/pie_population.png)
        * [bar_population.png](samples/tables_and_graphs/bar_population.png)
    3. Відображає в табличному вигляді основні стаститичні величини: min, max, mean, квантіли 25%, 75%, 95%:
        * [statistics_population.csv](samples/tables_and_graphs/statistics_population.csv)
        * [statistics_population.json](samples/tables_and_graphs/statistics_population.json)
        * [statistics_population.xlsx](samples/tables_and_graphs/statistics_population.xlsx)
    4. Показує по роках по кожній країні для відповідного варіанта зв'язок між іншими datasets (для яких є дані):
        
        I. зв'язок ціни на нафту з ppp:
          * [correlation_oil_ppp.csv](samples/tables_and_graphs/correlation_oil_ppp.csv)
          * [correlation_oil_ppp.json](samples/tables_and_graphs/correlation_oil_ppp.json)
          * [correlation_oil_ppp.xlsx](samples/tables_and_graphs/correlation_oil_ppp.xlsx)

        
        II. відсоток ppp окремої країни до середнього ppp всіх країн за рік:
          * [df_percentage_ppp.csv](samples/tables_and_graphs/df_percentage_ppp.csv)
          * [df_percentage_ppp.json](samples/tables_and_graphs/df_percentage_ppp.json)
          * [df_percentage_ppp.xlsx](samples/tables_and_graphs/df_percentage_ppp.xlsx)
        
        III. зв'язок популяції та ppp:
          * [correlation_population_ppp.csv](samples/tables_and_graphs/correlation_population_ppp.csv)
          * [correlation_population_ppp.json](samples/tables_and_graphs/correlation_population_ppp.json)
          * [correlation_population_ppp.xlsx](samples/tables_and_graphs/correlation_population_ppp.xlsx)
        
        IV. зв'язок популяції та цін на нафту:
          * [correlation_population_oil.csv](samples/tables_and_graphs/correlation_population_oil.csv)
          * [correlation_population_oil.json](samples/tables_and_graphs/correlation_population_oil.json)
          * [correlation_population_oil.xlsx](samples/tables_and_graphs/correlation_population_oil.xlsx)
       
