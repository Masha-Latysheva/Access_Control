CREATE TABLE "type"(
    "id" SERIAL PRIMARY KEY,
    "worktype" VARCHAR(128) NOT NULL
);
CREATE TABLE "job"(
    "id" SERIAL PRIMARY KEY,
    "jobtype" VARCHAR(128) NOT NULL
);
CREATE TABLE "structsub"(
    "id" SERIAL PRIMARY KEY,
    "structsub" VARCHAR(128) NOT NULL
);
CREATE TABLE "ref"(
    "id" SERIAL PRIMARY KEY,
    "ref" VARCHAR(128) NOT NULL
);
CREATE TABLE "user"(
    "id" SERIAL PRIMARY KEY,
    "fio" VARCHAR(128) NOT NULL,
    "type_id" INTEGER REFERENCES "type"("id"),
    "job_id" INTEGER REFERENCES "job"("id"),
    "structsub_id" INTEGER REFERENCES "structsub"("id"),
    "ref_id" INTEGER REFERENCES "ref"("id"),
    "phone" TEXT
);
CREATE TABLE "work"(
	"id" SERIAL PRIMARY KEY,
    "user_id" INTEGER REFERENCES "user"("id"),
    "type" INTEGER NOT NULL,
	"date" DATE NOT NULL
	
);
CREATE TABLE "uid"(
    "user_id" INTEGER REFERENCES "user"("id"),
    "uid" VARCHAR(128) PRIMARY KEY
);
CREATE TABLE "topic"(
    "topic" VARCHAR(128) PRIMARY KEY,
    "topic_name" VARCHAR(128) NOT NULL
);
CREATE TABLE "records"(
    "id" BIGSERIAL PRIMARY KEY,
    "uid" VARCHAR(128) NOT NULL,
    "data" DATE NOT NULL,
    "time" TIME(3) WITH TIME ZONE NOT NULL,
    "topic" VARCHAR(128) NOT NULL
);
CREATE TABLE "appRole"(
    "role" VARCHAR(128) PRIMARY KEY,
    "appau" BOOLEAN NOT NULL,
    "serverau" BOOLEAN NOT NULL,
    "dir_ed" BOOLEAN NOT NULL,
    "repo_on" BOOLEAN NOT NULL,
    "user_ed" BOOLEAN NOT NULL,
    "shed_ed" BOOLEAN NOT NULL,
	"set_app" BOOLEAN NOT NULL,
	"set_org" BOOLEAN NOT NULL,
	"set_repo" BOOLEAN NOT NULL,
	"set_user" BOOLEAN NOT NULL,
	"set_role" BOOLEAN NOT NULL,
    "set_serv" BOOLEAN NOT NULL,
    "set_view" BOOLEAN NOT NULL
);
CREATE TABLE "userApp"(
    "username" TEXT PRIMARY KEY,
    "password" TEXT NOT NULL,
    "role" VARCHAR(128) REFERENCES "appRole"("role"),
	"enable" BOOLEAN NOT NULL
);
CREATE TABLE "setUserApp"(
	"username" TEXT PRIMARY KEY REFERENCES "userApp"("username"),
    "parameter" TEXT NOT NULL,
    "attribute" TEXT NOT NULL
);
CREATE TABLE "organization"(
    "id" SERIAL PRIMARY KEY,
    "uid" VARCHAR(128) REFERENCES "uid"("uid"),
    "fio_id" INTEGER REFERENCES "user"("id"),
    "organization" VARCHAR(128) NOT NULL,
    "type_id" INTEGER REFERENCES "type"("id"),
    "structsub_id" INTEGER REFERENCES "structsub"("id"),
    "job_id" INTEGER REFERENCES "job"("id")
);