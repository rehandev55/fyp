import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../wayfinder'
/**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
export const dashboard = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: dashboard.url(options),
    method: 'get',
})

dashboard.definition = {
    methods: ["get","head"],
    url: '/admin/dashboard',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
dashboard.url = (options?: RouteQueryOptions) => {
    return dashboard.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
dashboard.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: dashboard.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
dashboard.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: dashboard.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
    const dashboardForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: dashboard.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
 */
        dashboardForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: dashboard.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\DashboardController::__invoke
 * @see app/Http/Controllers/Admin/DashboardController.php:10
 * @route '/admin/dashboard'
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
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
export const users = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: users.url(options),
    method: 'get',
})

users.definition = {
    methods: ["get","head"],
    url: '/admin/users',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
users.url = (options?: RouteQueryOptions) => {
    return users.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
users.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: users.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
users.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: users.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
    const usersForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: users.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
        usersForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: users.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:14
 * @route '/admin/users'
 */
        usersForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: users.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    users.form = usersForm
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
export const content = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: content.url(options),
    method: 'get',
})

content.definition = {
    methods: ["get","head"],
    url: '/admin/content',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
content.url = (options?: RouteQueryOptions) => {
    return content.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
content.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: content.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
content.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: content.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
    const contentForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: content.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
        contentForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: content.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:15
 * @route '/admin/content'
 */
        contentForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: content.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    content.form = contentForm
const admin = {
    dashboard: Object.assign(dashboard, dashboard),
users: Object.assign(users, users),
content: Object.assign(content, content),
}

export default admin