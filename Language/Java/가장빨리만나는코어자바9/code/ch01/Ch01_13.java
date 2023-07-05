package code.ch01;


import java.util.*;

public class Ch01_13 {
    /**
     * 13. 1~49 사이의 서로 다른 숫자를 여섯 개 골라 복권의 숫자 조합을 출력하는 프로그램을 작성하라.
     * (서로 다른 숫자를 여섯 개 골라낼려고 먼저 1...49로 채워진 배열 리스트를 만든다. 임의의 인덱스를 골라 해당하는 요소를 재거한다.
     * 이 작업을 여섯 번 반복한다. 그런 다음 결과를 정렬해 출력한다.)
     *
     * 새롭게 알게 된 것
     * 배열 Integer[] : 요소에 접근할 때 []연산자를 사용.
     * 배열 리스트 Array<> : 클래스이기 때문에 인스턴스 생성 문법과 메서드 호출 문법을 사용해서 접근
     */
    public static void randomLotto(){
        // 배열 생성
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=1;i<50;i++) { list.add(i); }

        // 결과 담을 list
        ArrayList<Integer> result = new ArrayList<>();
        // 1~49 사이의 랜덤 값 제거
        for (int i=0; i < 6; i++ ) {
            Random random = new Random();
            int idx = random.nextInt(list.size());

            // 결과 인서트
            result.add(list.get(idx));
            // 중복 제거를 위해 삭제
            list.remove(idx);
        }

        //정렬
        Collections.sort(result);
        System.out.println(result);
    }

    public static void main(String [] args) {
        randomLotto();
    }
}
