package com.project.controller;

import com.project.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.UUID;

@Controller
public class MainController {
    @GetMapping("/")
    public String greeting(Map<String, Object> model){
        return "main";
    }

    @GetMapping("/main")
    public String main(
            Model model,
            @AuthenticationPrincipal User user
    ){
        model.addAttribute("url","/main");
        return "main";
    }
    @GetMapping("/terminal")
    @PreAuthorize("hasAuthority('ADMIN')")
    public String terminal(
            Model model,
            @AuthenticationPrincipal User user
    ){
        model.addAttribute("url","/terminal");
        return "terminal";
    }
//    @PostMapping("/main")
//    public String add(
//            @AuthenticationPrincipal User user,
//            @RequestParam(value = "file", required = true) MultipartFile file,
//            BindingResult bindingResult,
//            Model model
//    ) throws IOException {
//        saveFile(file);
//        model.addAttribute("url","/main");
//        return "main";
//    }

//    private void saveFile(MultipartFile file) throws IOException {
//        if (file != null && !file.isEmpty() && file.getSize()!=0 && !file.getOriginalFilename().isEmpty() && !file.getOriginalFilename().equals("") && !file.getOriginalFilename().equals(" ")) {
//            File uploadDir = new File(uploadpath);
//
//            if (!uploadDir.exists()) {
//                uploadDir.mkdir();
//            }
//            String uuidFile = UUID.randomUUID().toString();
//
//            String resultFileName = uuidFile + "." +  file.getOriginalFilename();
//
//            file.transferTo(new File(uploadpath + "/" + resultFileName));
//        }
//    }




}