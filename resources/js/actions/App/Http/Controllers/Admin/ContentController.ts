import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition, applyUrlDefaults } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\Admin\ContentController::store
 * @see app/Http/Controllers/Admin/ContentController.php:23
 * @route '/api/content'
 */
export const store = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: store.url(options),
    method: 'post',
})

store.definition = {
    methods: ["post"],
    url: '/api/content',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::store
 * @see app/Http/Controllers/Admin/ContentController.php:23
 * @route '/api/content'
 */
store.url = (options?: RouteQueryOptions) => {
    return store.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::store
 * @see app/Http/Controllers/Admin/ContentController.php:23
 * @route '/api/content'
 */
store.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: store.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::store
 * @see app/Http/Controllers/Admin/ContentController.php:23
 * @route '/api/content'
 */
    const storeForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: store.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::store
 * @see app/Http/Controllers/Admin/ContentController.php:23
 * @route '/api/content'
 */
        storeForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: store.url(options),
            method: 'post',
        })
    
    store.form = storeForm
/**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
export const index = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: index.url(options),
    method: 'get',
})

index.definition = {
    methods: ["get","head"],
    url: '/api/content',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
index.url = (options?: RouteQueryOptions) => {
    return index.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
index.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: index.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
index.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: index.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
    const indexForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: index.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
        indexForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: index.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\ContentController::index
 * @see app/Http/Controllers/Admin/ContentController.php:54
 * @route '/api/content'
 */
        indexForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: index.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    index.form = indexForm
/**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
export const download = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: download.url(args, options),
    method: 'get',
})

download.definition = {
    methods: ["get","head"],
    url: '/api/content/download/{id}',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
download.url = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions) => {
    if (typeof args === 'string' || typeof args === 'number') {
        args = { id: args }
    }

    
    if (Array.isArray(args)) {
        args = {
                    id: args[0],
                }
    }

    args = applyUrlDefaults(args)

    const parsedArgs = {
                        id: args.id,
                }

    return download.definition.url
            .replace('{id}', parsedArgs.id.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
download.get = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: download.url(args, options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
download.head = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: download.url(args, options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
    const downloadForm = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: download.url(args, options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
        downloadForm.get = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: download.url(args, options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\ContentController::download
 * @see app/Http/Controllers/Admin/ContentController.php:65
 * @route '/api/content/download/{id}'
 */
        downloadForm.head = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: download.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    download.form = downloadForm
/**
* @see \App\Http\Controllers\Admin\ContentController::update
 * @see app/Http/Controllers/Admin/ContentController.php:86
 * @route '/api/content/{id}'
 */
export const update = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'put'> => ({
    url: update.url(args, options),
    method: 'put',
})

update.definition = {
    methods: ["put"],
    url: '/api/content/{id}',
} satisfies RouteDefinition<["put"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::update
 * @see app/Http/Controllers/Admin/ContentController.php:86
 * @route '/api/content/{id}'
 */
update.url = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions) => {
    if (typeof args === 'string' || typeof args === 'number') {
        args = { id: args }
    }

    
    if (Array.isArray(args)) {
        args = {
                    id: args[0],
                }
    }

    args = applyUrlDefaults(args)

    const parsedArgs = {
                        id: args.id,
                }

    return update.definition.url
            .replace('{id}', parsedArgs.id.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::update
 * @see app/Http/Controllers/Admin/ContentController.php:86
 * @route '/api/content/{id}'
 */
update.put = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'put'> => ({
    url: update.url(args, options),
    method: 'put',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::update
 * @see app/Http/Controllers/Admin/ContentController.php:86
 * @route '/api/content/{id}'
 */
    const updateForm = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: update.url(args, {
                    [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                        _method: 'PUT',
                        ...(options?.query ?? options?.mergeQuery ?? {}),
                    }
                }),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::update
 * @see app/Http/Controllers/Admin/ContentController.php:86
 * @route '/api/content/{id}'
 */
        updateForm.put = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: update.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'PUT',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'post',
        })
    
    update.form = updateForm
/**
* @see \App\Http\Controllers\Admin\ContentController::destroy
 * @see app/Http/Controllers/Admin/ContentController.php:76
 * @route '/api/content/{id}'
 */
export const destroy = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'delete'> => ({
    url: destroy.url(args, options),
    method: 'delete',
})

destroy.definition = {
    methods: ["delete"],
    url: '/api/content/{id}',
} satisfies RouteDefinition<["delete"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::destroy
 * @see app/Http/Controllers/Admin/ContentController.php:76
 * @route '/api/content/{id}'
 */
destroy.url = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions) => {
    if (typeof args === 'string' || typeof args === 'number') {
        args = { id: args }
    }

    
    if (Array.isArray(args)) {
        args = {
                    id: args[0],
                }
    }

    args = applyUrlDefaults(args)

    const parsedArgs = {
                        id: args.id,
                }

    return destroy.definition.url
            .replace('{id}', parsedArgs.id.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::destroy
 * @see app/Http/Controllers/Admin/ContentController.php:76
 * @route '/api/content/{id}'
 */
destroy.delete = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'delete'> => ({
    url: destroy.url(args, options),
    method: 'delete',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::destroy
 * @see app/Http/Controllers/Admin/ContentController.php:76
 * @route '/api/content/{id}'
 */
    const destroyForm = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: destroy.url(args, {
                    [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                        _method: 'DELETE',
                        ...(options?.query ?? options?.mergeQuery ?? {}),
                    }
                }),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::destroy
 * @see app/Http/Controllers/Admin/ContentController.php:76
 * @route '/api/content/{id}'
 */
        destroyForm.delete = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: destroy.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'DELETE',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'post',
        })
    
    destroy.form = destroyForm
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
const ContentController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ContentController.url(options),
    method: 'get',
})

ContentController.definition = {
    methods: ["get","head"],
    url: '/admin/content',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
ContentController.url = (options?: RouteQueryOptions) => {
    return ContentController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
ContentController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ContentController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
ContentController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: ContentController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
    const ContentControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: ContentController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
        ContentControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ContentController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:17
 * @route '/admin/content'
 */
        ContentControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ContentController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    ContentController.form = ContentControllerForm
ContentController.store = store
ContentController.index = index
ContentController.download = download
ContentController.update = update
ContentController.destroy = destroy

export default ContentController