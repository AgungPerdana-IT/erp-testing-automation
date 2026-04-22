from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


def input_text(driver, wait, by, locator, value):
    el = wait.until(EC.visibility_of_element_located((by, locator)))

    driver.execute_script("""
        const input = arguments[0];
        input.value = '';
        input.dispatchEvent(new Event('input', { bubbles: true }));
    """, el)

    el.send_keys(value)


def select_random(driver, wait, name_attr, exclude_zero=True):
    el = wait.until(EC.visibility_of_element_located((By.NAME, name_attr)))

    values = driver.execute_script("""
        return Array.from(arguments[0].options)
            .filter(o => arguments[1] ? o.value !== "0" : true)
            .map(o => o.value);
    """, el, exclude_zero)

    chosen = random.choice(values)

    driver.execute_script("""
        const select = arguments[0];
        select.value = arguments[1];
        select.dispatchEvent(new Event('change', { bubbles: true }));
        select.dispatchEvent(new Event('input', { bubbles: true }));
    """, el, chosen)

    wait.until(lambda d: el.get_attribute("value") == chosen)

    return chosen


def clear_and_fill(driver, wait, by, locator, value):
    element = wait.until(EC.presence_of_element_located((by, locator)))

    driver.execute_script("""
        const el = arguments[0];
        el.value = '';
        el.dispatchEvent(new Event('input', { bubbles: true }));
    """, element)

    element.send_keys(value)


def set_select_value(driver, element, value):
    driver.execute_script("""
        const select = arguments[0];
        select.value = arguments[1];
        select.dispatchEvent(new Event('change', { bubbles: true }));
        select.dispatchEvent(new Event('input', { bubbles: true }));
    """, element, value)


def select_parent(driver, wait):
    parent_element = wait.until(
        EC.visibility_of_element_located((By.NAME, "parent_id"))
    )

    values = driver.execute_script("""
        return Array.from(arguments[0].options)
            .filter(o => o.value !== "0")
            .map(o => o.value);
    """, parent_element)

    if not values:
        raise Exception("Tidak ada parent category valid!")

    chosen = random.choice(values)

    driver.execute_script("""
        const select = arguments[0];
        select.value = arguments[1];
        select.dispatchEvent(new Event('change', { bubbles: true }));
        select.dispatchEvent(new Event('input', { bubbles: true }));
    """, parent_element, chosen)

    wait.until(lambda d: parent_element.get_attribute("value") == chosen)

    print("Parent terpilih:", chosen)


def select_checkbox(driver, wait):
    customer = wait.until(EC.visibility_of_element_located((By.ID, "is_customer")))
    supplier = wait.until(EC.visibility_of_element_located((By.ID, "is_supplier")))

    choice = random.choice(["customer", "supplier", "both"])

    if choice == "customer":
        if not customer.is_selected():
            customer.click()
        if supplier.is_selected():
            supplier.click()

    elif choice == "supplier":
        if not supplier.is_selected():
            supplier.click()
        if customer.is_selected():
            customer.click()

    else:
        if not customer.is_selected():
            customer.click()
        if not supplier.is_selected():
            supplier.click()

    return choice