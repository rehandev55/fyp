import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
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
 * @see app/Http/Controllers/Admin/ContentController.php:10
 * @route '/admin/content'
 */
ContentController.url = (options?: RouteQueryOptions) => {
    return ContentController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
 * @route '/admin/content'
 */
ContentController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ContentController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
 * @route '/admin/content'
 */
ContentController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: ContentController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
 * @route '/admin/content'
 */
    const ContentControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: ContentController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
 * @route '/admin/content'
 */
        ContentControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ContentController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\ContentController::__invoke
 * @see app/Http/Controllers/Admin/ContentController.php:10
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
export default ContentController