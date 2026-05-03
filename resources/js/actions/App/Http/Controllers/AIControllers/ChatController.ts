import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition, applyUrlDefaults } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
export const sessions = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: sessions.url(options),
    method: 'get',
})

sessions.definition = {
    methods: ["get","head"],
    url: '/api/chat/sessions',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
sessions.url = (options?: RouteQueryOptions) => {
    return sessions.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
sessions.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: sessions.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
sessions.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: sessions.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
    const sessionsForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: sessions.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
        sessionsForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: sessions.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AIControllers\ChatController::sessions
 * @see app/Http/Controllers/AIControllers/ChatController.php:19
 * @route '/api/chat/sessions'
 */
        sessionsForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: sessions.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    sessions.form = sessionsForm
/**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
export const messages = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: messages.url(args, options),
    method: 'get',
})

messages.definition = {
    methods: ["get","head"],
    url: '/api/chat/messages/{id}',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
messages.url = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions) => {
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

    return messages.definition.url
            .replace('{id}', parsedArgs.id.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
messages.get = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: messages.url(args, options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
messages.head = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: messages.url(args, options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
    const messagesForm = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: messages.url(args, options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
        messagesForm.get = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: messages.url(args, options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AIControllers\ChatController::messages
 * @see app/Http/Controllers/AIControllers/ChatController.php:26
 * @route '/api/chat/messages/{id}'
 */
        messagesForm.head = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: messages.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    messages.form = messagesForm
/**
* @see \App\Http\Controllers\AIControllers\ChatController::send
 * @see app/Http/Controllers/AIControllers/ChatController.php:32
 * @route '/api/chat/send'
 */
export const send = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: send.url(options),
    method: 'post',
})

send.definition = {
    methods: ["post"],
    url: '/api/chat/send',
} satisfies RouteDefinition<["post"]>

/**
* @see \App\Http\Controllers\AIControllers\ChatController::send
 * @see app/Http/Controllers/AIControllers/ChatController.php:32
 * @route '/api/chat/send'
 */
send.url = (options?: RouteQueryOptions) => {
    return send.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\ChatController::send
 * @see app/Http/Controllers/AIControllers/ChatController.php:32
 * @route '/api/chat/send'
 */
send.post = (options?: RouteQueryOptions): RouteDefinition<'post'> => ({
    url: send.url(options),
    method: 'post',
})

    /**
* @see \App\Http\Controllers\AIControllers\ChatController::send
 * @see app/Http/Controllers/AIControllers/ChatController.php:32
 * @route '/api/chat/send'
 */
    const sendForm = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: send.url(options),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\ChatController::send
 * @see app/Http/Controllers/AIControllers/ChatController.php:32
 * @route '/api/chat/send'
 */
        sendForm.post = (options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: send.url(options),
            method: 'post',
        })
    
    send.form = sendForm
/**
* @see \App\Http\Controllers\AIControllers\ChatController::deleteMethod
 * @see app/Http/Controllers/AIControllers/ChatController.php:113
 * @route '/api/chat/{id}'
 */
export const deleteMethod = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'delete'> => ({
    url: deleteMethod.url(args, options),
    method: 'delete',
})

deleteMethod.definition = {
    methods: ["delete"],
    url: '/api/chat/{id}',
} satisfies RouteDefinition<["delete"]>

/**
* @see \App\Http\Controllers\AIControllers\ChatController::deleteMethod
 * @see app/Http/Controllers/AIControllers/ChatController.php:113
 * @route '/api/chat/{id}'
 */
deleteMethod.url = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions) => {
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

    return deleteMethod.definition.url
            .replace('{id}', parsedArgs.id.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\ChatController::deleteMethod
 * @see app/Http/Controllers/AIControllers/ChatController.php:113
 * @route '/api/chat/{id}'
 */
deleteMethod.delete = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'delete'> => ({
    url: deleteMethod.url(args, options),
    method: 'delete',
})

    /**
* @see \App\Http\Controllers\AIControllers\ChatController::deleteMethod
 * @see app/Http/Controllers/AIControllers/ChatController.php:113
 * @route '/api/chat/{id}'
 */
    const deleteMethodForm = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
        action: deleteMethod.url(args, {
                    [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                        _method: 'DELETE',
                        ...(options?.query ?? options?.mergeQuery ?? {}),
                    }
                }),
        method: 'post',
    })

            /**
* @see \App\Http\Controllers\AIControllers\ChatController::deleteMethod
 * @see app/Http/Controllers/AIControllers/ChatController.php:113
 * @route '/api/chat/{id}'
 */
        deleteMethodForm.delete = (args: { id: string | number } | [id: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'post'> => ({
            action: deleteMethod.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'DELETE',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'post',
        })
    
    deleteMethod.form = deleteMethodForm
/**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
export const history = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: history.url(args, options),
    method: 'get',
})

history.definition = {
    methods: ["get","head"],
    url: '/api/chat/history/{sessionId}',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
history.url = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions) => {
    if (typeof args === 'string' || typeof args === 'number') {
        args = { sessionId: args }
    }

    
    if (Array.isArray(args)) {
        args = {
                    sessionId: args[0],
                }
    }

    args = applyUrlDefaults(args)

    const parsedArgs = {
                        sessionId: args.sessionId,
                }

    return history.definition.url
            .replace('{sessionId}', parsedArgs.sessionId.toString())
            .replace(/\/+$/, '') + queryParams(options)
}

/**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
history.get = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: history.url(args, options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
history.head = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: history.url(args, options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
    const historyForm = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: history.url(args, options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
        historyForm.get = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: history.url(args, options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\AIControllers\ChatController::history
 * @see app/Http/Controllers/AIControllers/ChatController.php:121
 * @route '/api/chat/history/{sessionId}'
 */
        historyForm.head = (args: { sessionId: string | number } | [sessionId: string | number ] | string | number, options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: history.url(args, {
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    history.form = historyForm
const ChatController = { sessions, messages, send, deleteMethod, history, delete: deleteMethod }

export default ChatController