#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("""delete from t_rounds""")
    conn.commit()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from t_players")
    conn.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("""select count(player_id) as player_count
                     from t_players""")
    row = cur.fetchone()
    player_count = row[0]
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into t_players (player_name) values (%s)", (name,))
    conn.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""select p.player_id,
                          p.player_name,
                          count(rw.player_id_win) as player_wins,
                          count(rm.round_id) as player_matches
                     from t_players p
                       left outer join t_rounds rw
                         on (p.player_id = rw.player_id_win)
                       left outer join t_rounds rm
                         on ((p.player_id = rm.player_id_win)
                          or (p.player_id = rm.player_id_loss))
                   group by p.player_id, p.player_name
                   order by count(rw.player_id_win) desc
                """)
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)

    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
                insert into t_rounds (tourn_id, player_id_win, player_id_loss)
                values (1, %s, %s)""", (winner, loser, ))
    conn.commit()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
                select p1.player_id as player_1_id,
                       p1.player_name as player_1_name,
                       p2.player_id as player_2_id,
                       p2.player_name as player_2_name
                  from v_standings v1,
                       v_standings v2,
                       t_players p1,
                       t_players p2
                 where  (v1.player_rank < v2.player_rank
                     and v2.player_rank - v1.player_rank = 1)
                   and v1.player_id = p1.player_id
                   and v2.player_id = p2.player_id
                   and v1.player_wins = v2.player_wins
                """)
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)

    return results
