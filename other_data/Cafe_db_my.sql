CREATE TABLE "Cafes" ("Id" serial PRIMARY KEY NOT NULL,  "Name" text NOT NULL);

CREATE TABLE "Recipes" (
  "Id" serial PRIMARY KEY NOT NULL,
  "Name" text NOT NULL,
  "Deskription" text
);

CREATE TABLE "RecipeIngredients" (
  "Id" serial PRIMARY KEY NOT NULL,
  "RecipeID" int NOT NULL,
  "FoodProductID" int NOT NULL,
  "Number" float NOT NULL
);

CREATE TABLE "FoodProducts" (
  "Id" serial PRIMARY KEY NOT NULL,
  "Name" text NOT NULL
);

CREATE TABLE "Storage" (
  "Id" serial PRIMARY KEY NOT NULL,
  "CafeID" int NOT NULL,
  "FoodProductID" int NOT NULL,
  "Number" float NOT NULL
);

CREATE TABLE "Users" (
  "Id" serial PRIMARY KEY NOT NULL,
  "Login" text NOT NULL,
  "HashedPassword" text NOT NULL,
  "Name" text NOT NULL,
  "Surname" text NOT NULL,
  "Patronymic" text,
  "birthday" date NOT NULL,
  "Type" enum NOT NULL
);

CREATE TABLE "Employees" (
  "Id" serial PRIMARY KEY NOT NULL,
  "UserId" int NOT NULL,
  "CafeID" int NOT NULL,
  "Post" text NOT NULL
);

CREATE TABLE "Orders" (
  "Id" serial PRIMARY KEY NOT NULL,
  "CafeId" int NOT NULL,
  "UserId" int NOT NULL,
  "Deskription" text
);

CREATE TABLE "OrderItems" (
  "Id" serial PRIMARY KEY NOT NULL,
  "OrderId" int NOT NULL,
  "RecipeID" int NOT NULL,
  "UserId" int NOT NULL
);

CREATE TABLE "Feedbacks" (
  "Id" serial PRIMARY KEY NOT NULL,
  "UserId" int NOT NULL,
  "Text" text NOT NULL
);

ALTER TABLE "RecipeIngredients" ADD FOREIGN KEY ("RecipeID") REFERENCES "Recipes" ("Id");

ALTER TABLE "RecipeIngredients" ADD FOREIGN KEY ("FoodProductID") REFERENCES "FoodProducts" ("Id");

ALTER TABLE "Storage" ADD FOREIGN KEY ("CafeID") REFERENCES "Cafes" ("Id");

ALTER TABLE "Storage" ADD FOREIGN KEY ("FoodProductID") REFERENCES "FoodProducts" ("Id");

ALTER TABLE "Employees" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");

ALTER TABLE "Employees" ADD FOREIGN KEY ("CafeID") REFERENCES "Cafes" ("Id");

ALTER TABLE "Orders" ADD FOREIGN KEY ("CafeId") REFERENCES "Cafes" ("Id");

ALTER TABLE "Orders" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");

ALTER TABLE "OrderItems" ADD FOREIGN KEY ("OrderId") REFERENCES "Orders" ("Id");

ALTER TABLE "OrderItems" ADD FOREIGN KEY ("RecipeID") REFERENCES "Recipes" ("Id");

ALTER TABLE "OrderItems" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");

ALTER TABLE "Feedbacks" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");
