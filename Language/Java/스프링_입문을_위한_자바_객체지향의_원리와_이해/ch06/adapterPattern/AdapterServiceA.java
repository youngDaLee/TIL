package adapterPattern;

public class AdapterServiceA {
    ServiceA sb1 = new ServiceA();

    void runService() {
        sb1.runServiceA();
    }
}
