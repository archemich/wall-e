<#import "parts/common.ftlh" as c/>
<#import "parts/login.ftlh" as l/>

<@c.page>
    <div class="h5">
        <h5>Login Page</h5>
    </div>

    <#if message1??>
        <div class="alert alert-success" role="alert">
            ${message1}
        </div>
        <#else>
            <#if Session?? && Session.SPRING_SECURITY_LAST_EXCEPTION??>
                <div class="alert alert-danger" role="alert">
                    ${Session.SPRING_SECURITY_LAST_EXCEPTION.message}
                </div>
            </#if>
    </#if>
    <div class="mt-4">
        <@l.login_form "/login" true/>
    </div>
</@c.page>