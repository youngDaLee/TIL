package JavaAlgorithm.programmers;

import java.util.HashMap;

public class 달리기경주 {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};

        // Hash 생성
        HashMap<String, Integer> nameHash = new HashMap<>();
        HashMap<Integer, String> rankHash = new HashMap<>();
        for (int i=0;i < players.length;i++) {
            nameHash.put(players[i], i);
            rankHash.put(i, players[i]);
        }

        for (String name:callings) {
            int rank = nameHash.get(name);
            String faster_name = rankHash.get(rank-1);

            // 순서 변경
            nameHash.put(name, rank-1);
            nameHash.put(faster_name, rank);
            rankHash.put(rank, faster_name);
            rankHash.put(rank-1, name);
        }

        answer = rankHash.values().toArray(new String[0]);
        return answer;
    }
}
