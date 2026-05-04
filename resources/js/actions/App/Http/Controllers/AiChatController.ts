import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
const AiChatController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: AiChatController.url(options),
    method: 'get',
})

AiChatController.definition = {
    methods: ["get","head"],
    url: '/aichat',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
AiChatController.url = (options?: RouteQueryOptions) => {
    return AiChatController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
AiChatController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: AiChatController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
AiChatController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: AiChatController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
    const AiChatControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: AiChatController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
        AiChatControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: AiChatController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AiChatController::__invoke
 * @see app/Http/Controllers/AiChatController.php:9
 * @route '/aichat'
 */
        AiChatControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: AiChatController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    AiChatController.form = AiChatControllerForm
export default AiChatController