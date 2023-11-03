package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

import org.velezreyes.quiz.question6.Drink;

public class VendingMachineImpl implements VendingMachine{
  private Map<String, Drink> drinks;
  private Map<String, Integer> drinkPrices;

  private int balance;

  private static VendingMachineImpl instance;
  public VendingMachineImpl(){
    this.drinks = new HashMap<>();
    this.drinks.put("ScottCola", new DrinkImpl("ScottCola", true));
    this.drinks.put("KarenTea", new DrinkImpl("KarenTea", false));

    this.drinkPrices = new HashMap<>();
    this.drinkPrices.put("ScottCola", 75);
    this.drinkPrices.put("KarenTea", 100);

    this.balance = 0;
  }

  public static VendingMachine getInstance() {
    // Fix me!
    if(instance == null) {
      instance = new VendingMachineImpl();
    }

    return instance;
  }

  @Override
  public void insertQuarter() {
    this.balance += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if (!this.drinks.containsKey(name)) {
      throw new UnknownDrinkException();
    }
    int drinkPrice = getDrinkPrice(name); // Obtener el precio de la bebida (puedes implementar esta función)
    if (this.balance < drinkPrice) {
      throw new NotEnoughMoneyException();
    }
    this.balance -= drinkPrice;
    return this.drinks.get(name);
  }

  private int getDrinkPrice(String name) throws UnknownDrinkException {
    if (drinkPrices.containsKey(name)) {
      return drinkPrices.get(name);
    }
    throw new UnknownDrinkException();
  }


}


