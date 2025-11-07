create extension if not exists "uuid-ossp";

create table users (
  id uuid primary key default uuid_generate_v4(),
  email text unique
);

create table birth_charts (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references users(id),
  birth_data jsonb,
  chart jsonb,
  created_at timestamp default now()
);

create table interpretations (
  id serial primary key,
  key text,
  meaning text
);
