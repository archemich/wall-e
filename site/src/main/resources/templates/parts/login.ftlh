<#macro login_form path isLoginPage>
    <form action="${path}" method="post">
        <div class="form-group row">
            <label class="col-sm-2 col-form-label"> Логин: </label>
            <div class="col-sm-5">
                <input class="form-control ${(usernameError??)?string('is-invalid', '')}"
                       type="text"
                       name="username"
                       value="<#if user??>${user.username}</#if>"
                />
                <#if usernameError??>
                    <div class="invalid-feedback">
                        ${usernameError}
                    </div>
                </#if>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2 col-form-label">Пароль: </label>
            <div class="col-sm-5">
                <input class="form-control ${(passwordError??)?string('is-invalid', '')}"
                       type="password"
                       name="password"
                />
                <#if passwordError??>
                    <div class="invalid-feedback">
                        ${passwordError}
                    </div>
                </#if>
            </div>
        </div>
        <#if !isLoginPage>
            <div class="form-group row">
                <label class="col-sm-2 col-form-label">Confirm Password: </label>
                <div class="col-sm-5">
                    <input class="form-control ${(password2Error??)?string('is-invalid', '')}"
                           type="password"
                           name="password2"
                    />
                    <#if passwordError??>
                        <div class="invalid-feedback">
                            ${password2Error}
                        </div>
                    </#if>
                </div>
            </div>
            <div class="form-group row">
                <label class="col-sm-2 col-form-label">E-mail: </label>
                <div class="col-sm-5">
                    <input class="form-control ${(emailError??)?string('is-invalid', '')}"
                           type="email"
                           name="email"
                           placeholder="exmple@example.com"
                           value="<#if user??>${user.email}</#if>"
                    />
                    <#if emailError??>
                        <div class="invalid-feedback">
                            ${emailError}
                        </div>
                    </#if>
                    <small id="emailHelp" class="form-text text-muted">We'll never share your data with anyone else.</small>
                </div>
            </div>
            <div class="form-group row">
                <div class="g-recaptcha" data-sitekey="6Lc2gtgZAAAAADrI5UoR2I242jYdS9MMbQLfh__M"></div>
                <#if captchaError??>
                    <div class="alert alert-danger" role="alert">
                        ${captchaError}
                    </div>
                </#if>
            </div>
        </#if>
        <input type="hidden" name="_csrf" value="${_csrf.token}"/>
        <div>
            <input class="btn btn-primary mt-2" type="submit" value="<#if isLoginPage>Sign In<#else>Create</#if>"/>
        </div>
    </form>
</#macro>

<#macro logout>
    <form action="/logout" method="post">
        <input type="hidden" name="_csrf" value="${_csrf.token}"/>
        <button class="btn btn-primary mr-3" type="submit">Выход</button>
    </form>
</#macro>

<#macro login>
    <form action="/login" method="get">
        <button class="btn btn-primary mr-3" type="submit">Вход</button>
    </form>
</#macro>