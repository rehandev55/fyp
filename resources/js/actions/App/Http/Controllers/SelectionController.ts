import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
const SelectionController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: SelectionController.url(options),
    method: 'get',
})

SelectionController.definition = {
    methods: ["get","head"],
    url: '/selection',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
SelectionController.url = (options?: RouteQueryOptions) => {
    return SelectionController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
SelectionController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: SelectionController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
SelectionController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: SelectionController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
    const SelectionControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: SelectionController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
        SelectionControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: SelectionController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\SelectionController::__invoke
 * @see app/Http/Controllers/SelectionController.php:9
 * @route '/selection'
 */
        SelectionControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: SelectionController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    SelectionController.form = SelectionControllerForm
export default SelectionController