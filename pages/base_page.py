from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def find_element_by_locator(self, locator):
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators_text(self, locator_1, i_text):
        method, locator = locator_1
        locator = locator.format(i_text)
        return (method, locator)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop_chrome(self, locator_from, locator_to):
        from_element = self.find_element_with_wait(locator_from)
        to_element   = self.find_element_with_wait(locator_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()


    def drag_and_drop_firefox(self, locator_from, locator_to):
        source_element = self.find_element_with_wait(locator_from)
        target_element = self.find_element_with_wait(locator_to)
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);
                    
                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);

                    var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)

    def wait_change_value(self, locator, value):

        class element_has_other_value(object):

            def __init__(self, locator, value, outer_instance):
                self.locator        = locator
                self.value          = value
                self.outer_instance = outer_instance

            def __call__(self, driver):
                element = self.outer_instance.find_element_with_wait(self.locator)
                if element.text != self.value:
                    return element
                else:
                    return False

        element = WebDriverWait(self.driver, 10).until(element_has_other_value(locator, value, self))
        return element.text

    def get_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        order_status_elements = self.driver.find_elements(*locator)
        return order_status_elements