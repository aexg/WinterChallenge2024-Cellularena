import sys, subprocess, random, json, tempfile, os
if __name__ == '__main__':
    f, log_file = tempfile.mkstemp(prefix='log_')
    os.close(f)
    seed = random.randrange(0, 2**31)
    n_players = len(sys.argv) - 1
    cmd = 'java --add-opens java.base/java.lang=ALL-UNNAMED -jar -Dleague.level=5 winter-2024-sprawl-1.0-SNAPSHOT.jar' +  ''.join([f' -p{i} "{sys.argv[i]}"' for i in range(1, n_players+1)]) + f' -d seed={seed} -l "{log_file}"'
    task = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(log_file, 'r') as f:
        json_log = json.load(f)
    os.remove(log_file)
    p_scores = [int(json_log['scores'][str(i)]) for i in range(n_players)]
    rv = {}
    rv['ranks'] = [sum([int(p_score < p2_score) for p2_score in p_scores]) for p_score in p_scores] # assumes higher score is better
    rv['errors'] = [int(p_score < 0) for p_score in p_scores] # assumes negative score means error
    rv['test_data'] = {'seed': seed}
    rv['player_data'] = [{} for _ in range(n_players)]
    for player, key in enumerate([str(i) for i in range(n_players)]):
        for data in json_log['errors'][key]:
            if not data: continue
            for line in [line.strip() for line in data.split('\n')]:
                vs = line.split(' ')
                if len(vs) < 4: continue
                if vs[0] == '[TDATA]':  rv['test_data'][vs[1]] = vs[3]
                if vs[0] == '[PDATA]':  rv['player_data'][player][vs[1]] = vs[3]
                if vs[0] == '[PDATA+]': rv['player_data'][player][vs[1]] = rv['player_data'][player].get(vs[1], 0.0) + float(vs[3])            
    print(json.dumps(rv))
