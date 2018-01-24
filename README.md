Simple implementation of Diffi-Hellman algorithm, more detail on [wiki](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

Good explain of fast exponential computation [link](http://codetown.ru/plusplus/algoritm-vozvedeniya-v-stepen/);
And a bit more explanation at [habr](https://habrahabr.ru/post/144886/).

*How to execute*
- make virtual environment `virtualenv -p python3 venv`
- apply it env `. venv/bin/activate`
- install dependencies `pip install -r requirements.txt`
- run test `pytest`
- view how caesar algorithm works `python -m src.caesar`
- view how diffie-hellman works `python -m src.diffie_hellman`

After playing with code call `deactivate` to deactivate virtual environment

