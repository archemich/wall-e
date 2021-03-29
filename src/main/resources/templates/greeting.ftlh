<#import "parts/common.ftlh" as c/>

<@c.page>
    <#include  "parts/security.ftlh"/>
    <#if name == "guest">
        <h5>Доступ запрещен</h5>
        <#else>
        <h5>Привет, ${name}!</h5>
    </#if>


</@c.page>