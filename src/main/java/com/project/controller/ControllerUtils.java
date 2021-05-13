package com.project.controller;

import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;

import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public abstract class ControllerUtils {
    static Map<String, String> getErrors(BindingResult bindingResult) {
        Collector<FieldError, ?, Map<String, String>> fieldErrorMapCollector = Collectors.toMap(
                fieldError -> fieldError.getField() + "Error",
                FieldError::getDefaultMessage
        );
        Map <String,String> errorsMap = bindingResult.getFieldErrors().stream().collect(fieldErrorMapCollector);
        for (String s : errorsMap.keySet()) {
            System.out.println(s+" "+errorsMap.get(s));
        }
        return errorsMap;
    }
}
