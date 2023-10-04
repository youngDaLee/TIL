package templateCallbackPattern;

public class Client {
    // 익명 내부 전략을 사용... => 리팩토링을 하자...ㅠ
    public static void main(String[] args) {
        Soldier rambo = new Soldier();

        rambo.runContext(new Strategy() {
            @Override
            public void runStrategy() {
                System.out.println("총! 총총! 초초총!");
            }
        });

        rambo.runContext(new Strategy() {
            @Override
            public void runStrategy() {
                System.out.println("슉! 슈슉! 슉! 슈슈슉!");
            }
        });

        rambo.runContext(new Strategy() {
            @Override
            public void runStrategy() {
                System.out.println("도! 도도독! 도독! 도도독!");
            }
        });
    }
}
