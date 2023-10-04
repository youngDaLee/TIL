package templateCallbackPattern;

public class SoldierRefactor {
    void runContext(String weaponSound) {
        System.out.println("전투시작");
        executeWeapon(weaponSound);
        System.out.println("전투종료");
    }

    private Strategy executeWeapon(final String weaponSound) {
        return new Strategy() {
            @Override
            public void runStrategy() {
                System.out.println(weaponSound);
            }
        }
    }
}
