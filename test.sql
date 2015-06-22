select 

create or replace view v_standings as
select p.player_id,
       count(rw.player_id_win) as player_wins,
       count(rm.round_id) as player_matches,
       rank() over (order by count(rw.player_id_win) desc, p.player_id asc) as player_rank
  from t_players p
    left outer join t_rounds rw
      on (p.player_id = rw.player_id_win)
    left outer join t_rounds rm
      on ((p.player_id = rm.player_id_win) or
          (p.player_id = rm.player_id_loss))
 group by p.player_id
 order by count(rw.player_id_win) desc;


select p1.player_id as player_1_id,
       p1.player_name as player_1_name,
       v1.player_wins,
       p2.player_id as player_2_id,
       p2.player_name as player_2_name,
       v2.player_wins
  from v_standings v1,
       v_standings v2,
       t_players p1,
       t_players p2
 where (v1.player_rank < v2.player_rank and v2.player_rank - v1.player_rank = 1)
   and v1.player_id = p1.player_id
   and v2.player_id = p2.player_id
   and v1.player_wins = v2.player_wins
