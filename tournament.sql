-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
\c tournament;

drop table t_players;
create table t_players
(
    player_id serial primary key,
    player_name varchar(40)
);
create index t_players_idx1 on t_players (player_id);

drop table t_rounds;
create table t_rounds
(
    round_id serial primary key,
    tourn_id integer not null,
    player_id_win integer not null,
    player_id_loss integer not null
);
create index t_rounds_idx1 on t_rounds (round_id, tourn_id);

drop table t_tournaments;
create table t_tournaments
(
    tourn_id serial primary key,
    tourn_description varchar(80),
    tourn_date date,
    tourn_location varchar(80)
);
create index t_tournaments_idx1 on t_tournaments (tourn_id);

create view v_standings as
select p.player_id,
       count(rw.player_id_win) as player_wins,
       count(rm.round_id) as player_matches
  from t_players p
    left outer join t_rounds rw
      on (p.player_id = rw.player_id_win)
    left outer join t_rounds rm
      on ((p.player_id = rm.player_id_win) or
          (p.player_id = rm.player_id_loss))
 group by p.player_id
 order by count(rw.player_id_win) desc;
