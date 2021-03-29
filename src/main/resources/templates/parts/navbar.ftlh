<#include  "security.ftlh" />
<#import "login.ftlh" as l />
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="navbar-brand">::::))))</div>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" href="/">Панель управления</a>
            </li>
            <#if isAdmin>
                <li class="nav-item">
                    <a class="nav-link" href="/user">Управление пользователями</a>
                </li>
            </#if>
            <#if user??>
            </#if>
        </ul>
            <#if name!="guest">
                <@l.logout/>
            <#else>
                <@l.login/>
        </#if>
        <div class="navbar-text">${name}</div>
    </div>
</nav>