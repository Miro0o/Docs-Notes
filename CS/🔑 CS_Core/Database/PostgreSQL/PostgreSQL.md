# [PostgreSQL](https://www.postgresql.org)

[TOC]



PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

There is a wealth of information to be found describing how to [install](https://www.postgresql.org/download/)and [use](https://www.postgresql.org/docs/) PostgreSQL through the [official documentation](https://www.postgresql.org/docs/). The PostgreSQL community provides many helpful places to become familiar with the technology, discover how it works, and find career opportunities. Reach out to the community [here](https://www.postgresql.org/community/).



## Guides

### Resources

π [Documentation](https://www.postgresql.org/docs/)

[PostgreSQL ζη¨ -- θιΈ](https://www.runoob.com/postgresql/postgresql-tutorial.html)



### Intro

#### Deployment

(Brew, docker, .dmg , .zip ...)

> [3 Easy Steps to Install Docker PostgreSQL Environment](https://hevodata.com/learn/docker-postgresql/)
>
> [Official guides](https://hub.docker.com/_/postgres)



Docker for example: 

1. CLI command:

```shell
docker pull postgres
docker run --name postgresql \
-e POSTGRES_USER=myusername \
-e POSTGRES_PASSWORD=mypassword \
-p 5432:5432 \
-v /data:/var/lib/postgresql/data \
-d postgres

docker run --name psql_test \
-e POSTGRES_USER=testuser \
-e POSTGRES_PASSWORD=mypassword \
-p 5432:5432 \
-v postgres_test_db:/var/lib/postgresql/data \
-d postgres

```

2. Docker-compose.yaml: 

```yaml
# Use postgres/example user/password as credentials

version: '3.1'

  services:

    db:											# PostgreSQL DMS
      image: postgres
      restart: always
      ports:
        - 5432:5432
      environment:
        POSTGRES_USER: example_username
        POSTGRES_PASSWORD: example_password
      network:
        PSQLnet

    adminer:
      image: adminer  							# PostgreSQL Web UI (optional)
      restart: always
      ports:
        - 8080:8080
      network:
        PSQLnet

    network:
      - PSQLnet
```

   



#### Cnfig

```shell
jdbc:postgresql://host:port/database
```



#### Usage

 [PostgreSQLζδ½-psqlεΊζ¬ε½δ»€](https://www.cnblogs.com/my-blogs-for-everone/p/10226473.html) 





#### Links:

[ηθ§£PostgreSQLζ°ζ?εΊγζ¨‘εΌγθ‘¨γη©Ίι΄γη¨ζ·ι΄ηε³η³»]:https://aozsky.com/database/postgresql.schema
[PostgreSQL ζ¨‘εΌοΌSCHEMAοΌ]:https://www.runoob.com/postgresql/postgresql-schema.html
[PostgreSQL JDBCε?’ζ·η«―ζ₯ε£δ»η»]:https://www.modb.pro/db/52381
[sonarqubeιη½?postgresqlζ°ζ?εΊ]:https://blog.51cto.com/huny/3263674

