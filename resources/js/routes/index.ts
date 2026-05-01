import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../wayfinder'
import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../wayfinder'
/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
export const login = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: login.url(options),
    method: 'get',
})

login.definition = {
    methods: ["get","head"],
    url: '/login',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
login.url = (options?: RouteQueryOptions) => {
    return login.definition.url + queryParams(options)
}

/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
login.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: login.url(options),
    method: 'get',
})
/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
login.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: login.url(options),
    method: 'head',
})

    /**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
    const loginForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: login.url(options),
        method: 'get',
    })

            /**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
        loginForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: login.url(options),
            method: 'get',
        })
            /**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::login
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:47
 * @route '/login'
 */
        loginForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: login.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    login.form = loginForm
/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::logout
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:100
 * @route '/logout'
 */
export const logout = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: logout.url(options),
    method: 'post',
})

logout.definition = {
    methods: ["post"],
    url: '/logout',
} satisfies RouteDefinition<["post"]>

/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::logout
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:100
 * @route '/logout'
 */
logout.url = (options?: RouteQueryOptions) => {
    return logout.definition.url + queryParams(options)
}

/**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::logout
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:100
 * @route '/logout'
 */
logout.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: logout.url(options),
    method: 'post',
})

    /**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::logout
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:100
 * @route '/logout'
 */
    const logoutForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: logout.url(options),
        method: 'post',
    })

            /**
* @see \Laravel\Fortify\Http\Controllers\AuthenticatedSessionController::logout
 * @see vendor/laravel/fortify/src/Http/Controllers/AuthenticatedSessionController.php:100
 * @route '/logout'
 */
        logoutForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: logout.url(options),
            method: 'post',
        })
    
    logout.form = logoutForm
/**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
export const register = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: register.url(options),
    method: 'get',
})

register.definition = {
    methods: ["get","head"],
    url: '/register',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
register.url = (options?: RouteQueryOptions) => {
    return register.definition.url + queryParams(options)
}

/**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
register.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: register.url(options),
    method: 'get',
})
/**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
register.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: register.url(options),
    method: 'head',
})

    /**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
    const registerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: register.url(options),
        method: 'get',
    })

            /**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
        registerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: register.url(options),
            method: 'get',
        })
            /**
* @see \Laravel\Fortify\Http\Controllers\RegisteredUserController::register
 * @see vendor/laravel/fortify/src/Http/Controllers/RegisteredUserController.php:41
 * @route '/register'
 */
        registerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: register.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    register.form = registerForm
/**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
export const home = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: home.url(options),
    method: 'get',
})

home.definition = {
    methods: ["get","head"],
    url: '/',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
home.url = (options?: RouteQueryOptions) => {
    return home.definition.url + queryParams(options)
}

/**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
home.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: home.url(options),
    method: 'get',
})
/**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
home.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: home.url(options),
    method: 'head',
})

    /**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
    const homeForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: home.url(options),
        method: 'get',
    })

            /**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
        homeForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: home.url(options),
            method: 'get',
        })
            /**
* @see \Inertia\Controller::__invoke
 * @see vendor/inertiajs/inertia-laravel/src/Controller.php:13
 * @route '/'
 */
        homeForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: home.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    home.form = homeForm
/**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
export const dashboard = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: dashboard.url(options),
    method: 'get',
})

dashboard.definition = {
    methods: ["get","head"],
    url: '/dashboard',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
dashboard.url = (options?: RouteQueryOptions) => {
    return dashboard.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
dashboard.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: dashboard.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
dashboard.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: dashboard.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
    const dashboardForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: dashboard.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
        dashboardForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: dashboard.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\DashboardController::__invoke
 * @see app/Http/Controllers/DashboardController.php:9
 * @route '/dashboard'
 */
        dashboardForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: dashboard.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    dashboard.form = dashboardForm
/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
export const selection = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: selection.url(options),
    method: 'get',
})

selection.definition = {
    methods: ["get","head"],
    url: '/selection',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
selection.url = (options?: RouteQueryOptions) => {
    return selection.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
selection.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: selection.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
selection.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: selection.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
    const selectionForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: selection.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
        selectionForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: selection.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
        selectionForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: selection.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    selection.form = selectionForm
/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
export const aichat = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: aichat.url(options),
    method: 'get',
})

aichat.definition = {
    methods: ["get","head"],
    url: '/aichat',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
aichat.url = (options?: RouteQueryOptions) => {
    return aichat.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
aichat.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: aichat.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
aichat.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: aichat.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
    const aichatForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: aichat.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
        aichatForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: aichat.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
        aichatForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: aichat.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    aichat.form = aichatForm
/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
export const practice = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: practice.url(options),
    method: 'get',
})

practice.definition = {
    methods: ["get","head"],
    url: '/practice',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
practice.url = (options?: RouteQueryOptions) => {
    return practice.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
practice.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: practice.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
practice.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: practice.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
    const practiceForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: practice.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
        practiceForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: practice.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
        practiceForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: practice.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    practice.form = practiceForm
/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
export const resources = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: resources.url(options),
    method: 'get',
})

resources.definition = {
    methods: ["get","head"],
    url: '/resources',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
resources.url = (options?: RouteQueryOptions) => {
    return resources.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
resources.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: resources.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
resources.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: resources.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
    const resourcesForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: resources.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
        resourcesForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: resources.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:10
 * @route '/resources'
 */
        resourcesForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: resources.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    resources.form = resourcesForm
/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
export const progress = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: progress.url(options),
    method: 'get',
})

progress.definition = {
    methods: ["get","head"],
    url: '/progress',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
progress.url = (options?: RouteQueryOptions) => {
    return progress.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
progress.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: progress.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
progress.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: progress.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
    const progressForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: progress.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
        progressForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: progress.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
        progressForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: progress.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    progress.form = progressForm
/**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
export const profile = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: profile.url(options),
    method: 'get',
})

profile.definition = {
    methods: ["get","head"],
    url: '/profile',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
profile.url = (options?: RouteQueryOptions) => {
    return profile.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
profile.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: profile.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
profile.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: profile.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
    const profileForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: profile.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
        profileForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: profile.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ProfileController::profile
 * @see app/Http/Controllers/ProfileController.php:15
 * @route '/profile'
 */
        profileForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: profile.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    profile.form = profileForm
/**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
export const about = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: about.url(options),
    method: 'get',
})

about.definition = {
    methods: ["get","head"],
    url: '/about',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
about.url = (options?: RouteQueryOptions) => {
    return about.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
about.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: about.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
about.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: about.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
    const aboutForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: about.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
        aboutForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: about.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AboutController::__invoke
 * @see app/Http/Controllers/AboutController.php:9
 * @route '/about'
 */
        aboutForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: about.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    about.form = aboutForm