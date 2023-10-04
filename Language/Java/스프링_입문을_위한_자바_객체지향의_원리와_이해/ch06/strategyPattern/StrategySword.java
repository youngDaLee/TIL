package strategyPattern;

public class StrategySword implements Strategy{
    @Override
    public void runStrategy() {
        System.out.println("슉, 슈슉, 슉, 슈슈슉");
    }
}
