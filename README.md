[![CircleCI](https://dl.circleci.com/status-badge/img/gh/lsmhun/cbsg-java/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/lsmhun/cbsg-java/tree/main)

# Corporate Bullshit Generator but even lazier

This is a fork of the [Corporate-Bullshit-Generator-for-Java] but with AI corrections to sound more professional even faster. 
Java implementation is based on [franciscouzo](https://github.com/franciscouzo/corporate_bullshit)'s 
Python code.

## Usage Java

Simple run `java -jar cbsg-0.1.0.jar` then "short workshop" will be generated.
there are some supported parameters for dedicated workspace influencers.

```shell
java -jar cbsg-0.1.0.jar --help

Available options:
--workshop
--shortWorkshop
--financialReport
--sentenceGuaranteedAmount=<ANY_INTEGER>

--configurationProperties=<DICTIONARY_PROPERTIES_FROM_CLASSPATH>
--help

```

## Usage Python

Create a file named ```openai.key``` then put your private key in it.
After running the Java code run this command.

```
python ai.py
```

## Examples

```
Sustainability in the digital age calls for a wave of change. The Chief Officer leverages the centralized and multi-tasked guidelines across boundaries. The long-term and holistic solutions solve our customer-centric, front-end analytics across and beyond the cubes. A consumer-facing and user-driven knowledge transfer enhances a customized and integrated sphere across the wider Group. The request/solution engineers a matrix, paving the way for compliant and mindful synergies; while the silo champion facilitates macroscopic and systematized style guidelines downstream.
```

## Documentation for [Corporate-Bullshit-Generator-for-Java]

Our mentor is still: [Dilbert](https://www.dilbert.com)'s pointy-haired boss

![Dilbert's pointy-haired boss](/docs/dilbert_pointy_haired_boss_01.webp)

- [English documentation](docs/descr_en.md)
- [Hungarian documentation](docs/descr_hu.md)
