package code.ch01;

import java.util.ArrayList;

public class Ch01_16 {
    /**
     * 16. average 매서드를 개선하여 매개변수를 적어도 한 개 이상 받으면 호출되게 해라
     */
    public static void main(String[] args){
        ArrayList<Double> list = new ArrayList<>();
        for (String a : args) {
            Double da = Double.valueOf(a);
            list.add(da);
        }

        double avg = average(list);
        System.out.println(avg);
    }

    public static double average(ArrayList<Double> list) {
        double sum = 0;
        for (double d : list){
            sum += d;
        }
        return sum / list.size();
    }
}
