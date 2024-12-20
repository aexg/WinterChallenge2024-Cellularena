# CodinCame Winter Challenge 2024 Cellularena CLI runner

This is a referee for CodinGame's Winter Challenge 2024 with command line interface adapted for usage with [cg-brutaltester](https://github.com/dreignier/cg-brutaltester)

https://www.codingame.com/contests/winter-challenge-2024

## Build

- install Java 17 and Maven
- run in command line `mvn package` in the root dir where pom.xml file is

The compiled jar file is in ./target/winter-2024-sprawl-1.0-SNAPSHOT.jar

## Run

Build cg-brutaltester as described in its readme-file ([cg-brutaltester](https://github.com/dreignier/cg-brutaltester))

To copy both referee and cg-brutaltester JAR files, i.e. winter-2024-sprawl-1.0-SNAPSHOT.jar and cg-brutaltester-1.0.0-SNAPSHOT.jar to same directory make handling paths easier.

This is a sample command that works, you can change optptions as described in the BrutalTester readme-file.

```
java -jar cg-brutaltester-1.0.0-SNAPSHOT.jar \
    -r "java --add-opens java.base/java.lang=ALL-UNNAMED -jar -Dleague.level=5 winter-2024-sprawl-1.0-SNAPSHOT.jar" \
    -p1 "python3 player1.py" \
    -p2 "python3 player2.py" \
    -s     \
    -t 4   \
    -n 10
```

Option `-Dleague.level=5` above defines League-5 that is valid for Bronze and higher leagues.

---
