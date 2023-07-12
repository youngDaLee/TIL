package code.ch02;

/**
 * 평면에 놓인점을 기술하는 불변 클래스 Point를 구현하라. 특정 점으로 설정하는 생성자와 원점으로 설정하는 인수 없는 생성자 getX,getY,translate, scale 메서드를구현하라.
 * translate 메서드는 x와 y 방향으로 주어진 길이만큼 점을 올긴다.
 * scale 메서드는 주어진 비율로 두 좌표의 크기를 조절한다.
 * 결과로 새로운 점을 반환하도록 이 메서드를 구현하라. 예를 들어 다음 문장은 p를 (2, 3.5) 좌표에 있는 점으로 설정해야 한다.
 * Point p = new Point(3,4).translate(1,3).scale(0.5);
 */
public class Ch02_5 {
    public double x;
    public double y;

    /**
     * 생성자
     * @param x
     * @param y
     */
    public Ch02_5(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * 인수없는 생성자
     */
    public Ch02_5() {
        this.x = 0;
        this.y = 0;
    }

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public void translate(int x, int y) {
        this.x += x;
        this.y += y;
    }

    public void scale(double s) {
        this.x *= s;
        this.y *= s;
    }

    public static void main(String[] args) {
        Ch02_5 point = new Ch02_5(3,4);
        point.translate(1,3);
        point.scale(0.5);

        System.out.println(point.getX()+", "+point.getY());
    }
}
